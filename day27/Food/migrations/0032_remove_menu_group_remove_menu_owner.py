# Generated by Django 4.1.5 on 2023-03-05 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0031_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="group",
        ),
        migrations.RemoveField(
            model_name="menu",
            name="owner",
        ),
    ]