# Generated by Django 2.2.10 on 2021-05-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_auto_membership_rename_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='po_box',
            new_name='postal_code',
        ),
    ]
