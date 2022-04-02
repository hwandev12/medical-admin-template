# Generated by Django 3.2 on 2022-04-02 10:08

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('records_feed', '0005_remove_setter_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='setter',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
