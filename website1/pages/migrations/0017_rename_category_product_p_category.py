# Generated by Django 5.0.1 on 2024-03-04 11:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0016_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="category",
            new_name="p_category",
        ),
    ]