# Generated by Django 4.1.5 on 2023-02-11 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0013_book_book"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Book",
        ),
        migrations.DeleteModel(
            name="Foo",
        ),
    ]
