# Generated by Django 4.1.5 on 2023-02-05 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Phone", "0005_rename_brand_brands_rename_color_colors_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Brands",
            new_name="Brand",
        ),
        migrations.RenameModel(
            old_name="Colors",
            new_name="Color",
        ),
        migrations.RenameModel(
            old_name="Models",
            new_name="Model",
        ),
        migrations.RenameModel(
            old_name="Recordings",
            new_name="Recording",
        ),
    ]
