# Generated by Django 4.2.5 on 2024-03-19 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0004_alter_orderitem_pdf_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="paid",
            field=models.BooleanField(null=True),
        ),
    ]
