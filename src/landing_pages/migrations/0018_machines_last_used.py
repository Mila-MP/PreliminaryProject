# Generated by Django 4.2.7 on 2023-11-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing_pages", "0017_machines_remaining_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="machines",
            name="last_used",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
