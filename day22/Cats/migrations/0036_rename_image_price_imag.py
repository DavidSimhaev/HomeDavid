# Generated by Django 4.1.5 on 2023-02-13 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0035_remove_price_file_price_image_alter_image_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="price",
            old_name="image",
            new_name="imag",
        ),
    ]
