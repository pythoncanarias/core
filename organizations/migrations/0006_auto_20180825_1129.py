# Generated by Django 2.1 on 2018-08-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_auto_20180825_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationcategory',
            name='code',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='organizationrole',
            name='code',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
