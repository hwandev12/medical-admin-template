# Generated by Django 3.2 on 2022-04-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records_feed', '0003_remove_setter_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='setter',
            name='contact_number',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]