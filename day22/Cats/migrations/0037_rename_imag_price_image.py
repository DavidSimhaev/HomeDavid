# Generated by Django 4.1.5 on 2023-02-13 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0036_rename_image_price_imag"),
    ]

    operations = [
        migrations.RenameField(
            model_name="price",
            old_name="imag",
            new_name="image",
        ),
    ]
