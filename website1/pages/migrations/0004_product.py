# Generated by Django 5.0.1 on 2024-01-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0003_register"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("p_name", models.CharField(max_length=255)),
                ("p_price", models.CharField(max_length=255)),
                ("p_image", models.FileField(upload_to="")),
            ],
        ),
    ]
