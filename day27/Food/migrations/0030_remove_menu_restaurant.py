# Generated by Django 4.1.5 on 2023-03-04 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0029_menu_restaurant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="restaurant",
        ),
    ]
