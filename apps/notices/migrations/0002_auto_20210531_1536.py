# Generated by Django 2.2.10 on 2021-05-31 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticekind',
            name='template',
            field=models.TextField(max_length=512),
        ),
    ]
