# Generated by Django 4.2.7 on 2023-11-13 17:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("landing_pages", "0009_machines_timestamp_machines_updated"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Machines",
        ),
    ]
