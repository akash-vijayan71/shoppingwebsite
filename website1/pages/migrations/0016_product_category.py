# Generated by Django 5.0.1 on 2024-03-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0015_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
