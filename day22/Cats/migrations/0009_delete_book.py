# Generated by Django 4.1.5 on 2023-02-10 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0008_book"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Book",
        ),
    ]
