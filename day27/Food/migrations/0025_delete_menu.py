# Generated by Django 4.1.5 on 2023-03-04 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0024_menu"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Menu",
        ),
    ]