# Generated by Django 4.2.7 on 2023-12-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing_pages", "0020_recipes_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
            ],
        ),
    ]
