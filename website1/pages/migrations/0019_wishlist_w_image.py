# Generated by Django 5.0.1 on 2024-03-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0018_wishlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="w_image",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
