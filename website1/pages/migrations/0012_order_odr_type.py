# Generated by Django 5.0.1 on 2024-02-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0011_order_odr_address_order_odr_billname_order_odr_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="odr_type",
            field=models.CharField(max_length=10, null=True),
        ),
    ]