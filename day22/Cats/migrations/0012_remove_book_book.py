# Generated by Django 4.1.5 on 2023-02-11 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0011_foo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="book",
        ),
    ]
