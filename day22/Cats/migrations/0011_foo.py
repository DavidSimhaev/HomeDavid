# Generated by Django 4.1.5 on 2023-02-11 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0010_book"),
    ]

    operations = [
        migrations.CreateModel(
            name="Foo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("audio", models.FilePathField(path="/home/user/")),
            ],
        ),
    ]
