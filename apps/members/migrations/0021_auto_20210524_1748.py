# Generated by Django 2.2.10 on 2021-05-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_auto_20191202_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='po_box',
            new_name='postal_code',
        ),
    ]
