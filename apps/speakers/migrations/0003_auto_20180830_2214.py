# Generated by Django 2.1 on 2018-08-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20180830_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(blank=True, upload_to='speakers/speaker/'),
        ),
    ]