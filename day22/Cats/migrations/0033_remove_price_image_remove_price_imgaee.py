# Generated by Django 4.1.5 on 2023-02-13 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0032_price_imgaee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="image",
        ),
        migrations.RemoveField(
            model_name="price",
            name="imgaee",
        ),
    ]
