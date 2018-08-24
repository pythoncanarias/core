# Generated by Django 2.1 on 2018-08-24 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=16, unique=True)),
                ('base_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
                ('bio', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=32)),
                ('photo', models.ImageField(blank=True, upload_to='speakers/speaker/')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contacts', to='speakers.Social'),
        ),
        migrations.AddField(
            model_name='contact',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contacts', to='speakers.Speaker'),
        ),
    ]
