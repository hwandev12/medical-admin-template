# Generated by Django 3.2 on 2022-04-02 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records_feed', '0002_auto_20220402_0441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setter',
            name='contact_number',
        ),
    ]
