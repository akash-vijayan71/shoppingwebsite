# Generated by Django 5.0.1 on 2024-03-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0020_product_p_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="p_disprice",
            field=models.FloatField(null=True),
        ),
    ]