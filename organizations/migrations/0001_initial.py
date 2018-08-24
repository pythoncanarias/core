# Generated by Django 2.1 on 2018-08-24 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(choices=[(10, 'High'), (50, 'Medium (default)'), (100, 'Low')], default=50)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('logo', models.ImageField(upload_to='organizations/sponsor/')),
                ('url', models.URLField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('management_email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(choices=[(10, 'High'), (50, 'Medium (default)'), (100, 'Low')], default=50)),
                ('code', models.CharField(max_length=16, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(choices=[(10, 'High'), (50, 'Medium (default)'), (100, 'Low')], default=50)),
                ('code', models.CharField(max_length=16, unique=True)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='organizations/group/')),
            ],
        ),
        migrations.AddField(
            model_name='organizationcategory',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='organization_categories', to='organizations.OrganizationSubcategory'),
        ),
        migrations.AddField(
            model_name='membership',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='memberships', to='organizations.OrganizationCategory'),
        ),
        migrations.AddField(
            model_name='membership',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='memberships', to='events.Event'),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='memberships', to='organizations.Organization'),
        ),
    ]
