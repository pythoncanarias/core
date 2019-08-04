from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin

from certificates.utils import create_certificate
from events.tasks import send_ticket

from .admin_inlines import ArticleInline, PresentInline
from .models import Article, Present, Raffle, Ticket, TicketCategory


@admin.register(TicketCategory)
class TicketCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name', ), }


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['event']
    list_display = (
        'event', 'category', 'price', 'stock',
        'sold_vs_available',
        'release_at', 'is_active',
        )

    def sold_vs_available(self, obj):
        return "{}/{}".format(
            obj.num_sold_tickets,
            obj.num_available_tickets,
            )


@admin.register(Ticket)
class TicketAdmin(ImportExportActionModelAdmin):
    list_display = (
        'customer_email', 'full_name', 'number',
        'sold_at', 'is_mail_send'
        )
    search_fields = (
        'customer_email',
        'customer_name',
        'customer_surname',
        'keycode',
        'number',
        )
    ordering = ('-sold_at', '-number')
    list_filter = ('article', 'sold_at', )

    def full_name(self, obj):
        return "{}, {}".format(
            obj.customer_surname,
            obj.customer_name,
            )

    def is_mail_send(self, obj):
        return bool(obj.sold_at)

    is_mail_send.boolean = True

    def resend_ticket_force(self, request, queryset):
        for ticket in queryset:
            send_ticket.delay(ticket, force=True)

    resend_ticket_force.short_description = "Recreate and send ticket"

    def resend_ticket(self, request, queryset):
        for ticket in queryset:
            send_ticket.delay(ticket)

    resend_ticket.short_description = "Resend ticket"

    def download_emails(self, request, queryset):
        distinct_emails = queryset.order_by().values_list(
            'customer_email', flat=True).distinct()
        content = ','.join(distinct_emails)
        filename = 'emails.txt'
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            filename)
        return response

    download_emails.short_description = "Download customers' emails"

    def gen_certificate(self, request, queryset):
        for ticket in queryset:
            create_certificate(
                'attendance',
                output_name=ticket.keycode,
                name=ticket.customer_full_name,
                )

    gen_certificate.short_description = 'Generar certificado de asistencia'

    actions = [
        resend_ticket,
        resend_ticket_force,
        download_emails,
        gen_certificate,
        ]


@admin.register(Raffle)
class RaffleAdmin(admin.ModelAdmin):
    inlines = [PresentInline]
    pass


@admin.register(Present)
class PresentAdmin(admin.ModelAdmin):
    pass
