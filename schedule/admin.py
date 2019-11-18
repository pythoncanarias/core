from django import forms
from django.contrib import admin
from django.http import HttpResponse

from .models import Schedule, Slot, SlotCategory, SlotLevel, SlotTag, Track
from locations.models import Location


class ScheduleInline(admin.StackedInline):
    model = Schedule
    extra = 0
    autocomplete_fields = ['speakers']


@admin.register(SlotCategory)
class SlotCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'code': ('name', ), }
    list_display = ('name', 'code')


@admin.register(SlotTag)
class SlotTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }
    list_display = ('name', 'slug')


@admin.register(SlotLevel)
class SlotLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    def has_slides(self, obj):
        return obj.slides != ''
    has_slides.boolean = True

    inlines = [ScheduleInline]
    list_display = ('name', 'has_slides', 'level', '_tags')
    search_fields = ['name']
    list_filter = ['level', 'tags']

    def _tags(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


class LocationChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name} - {obj.venue}'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ['event__name', 'location__name', 'slot__name',
                     'track__name', 'speakers__name', 'speakers__surname']
    list_display = ('slot', 'event', 'location', 'start')
    autocomplete_fields = ['speakers', 'slot']
    list_filter = ['event']

    def download_speakers_emails(self, request, queryset):
        emails = set()
        for schedule in queryset:
            schedule_emails = schedule.speakers.all().values_list(
                'email', flat=True)
            if schedule_emails:
                emails.add(*schedule_emails)
        content = ','.join(emails)
        filename = 'emails.txt'
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            filename)
        return response

    download_speakers_emails.short_description = "Download speakers' emails"

    actions = [download_speakers_emails, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'location':
            return LocationChoiceField(
                queryset=Location.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
