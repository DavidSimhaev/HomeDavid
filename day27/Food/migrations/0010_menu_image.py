# Generated by Django 4.1.5 on 2023-03-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0009_remove_menu_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="image",
            field=models.ImageField(max_length=255, null=True, upload_to="images/"),
        ),
    ]
