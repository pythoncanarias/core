# Generated by Django 2.2.7 on 2019-12-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20191201_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='fee_payment_type',
            field=models.CharField(blank=True, choices=[('BT', 'Transferencia bancaria'), ('ST', 'Stripe'), ('PP', 'PayPal')], default='BT', max_length=2),
        ),
    ]
