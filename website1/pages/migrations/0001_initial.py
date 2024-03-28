# Generated by Django 5.0.1 on 2024-01-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("contact_email", models.EmailField(max_length=255)),
                ("contact_name", models.TextField()),
            ],
        ),
    ]
