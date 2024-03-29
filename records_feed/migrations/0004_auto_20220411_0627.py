# Generated by Django 3.2 on 2022-04-11 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('records_feed', '0003_remove_setter_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setter',
            name='country',
        ),
        migrations.AddField(
            model_name='setter',
            name='contact_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setter',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
