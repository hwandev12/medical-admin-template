# Generated by Django 3.2 on 2022-04-02 04:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('records_feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setter',
            name='contact_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setter',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setter',
            name='message',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
