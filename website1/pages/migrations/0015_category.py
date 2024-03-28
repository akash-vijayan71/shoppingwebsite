# Generated by Django 5.0.1 on 2024-03-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0014_adminlogin_ad_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("c_name", models.CharField(max_length=255, null=True)),
                ("c_image", models.FileField(upload_to="")),
            ],
        ),
    ]