# Generated by Django 4.2.5 on 2023-12-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0010_delete_text_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="binoculars",
            name="hand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="lightings",
            name="hand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="tripods",
            name="hand",
            field=models.BooleanField(default=True),
        ),
    ]