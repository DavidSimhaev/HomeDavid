# Generated by Django 4.1.5 on 2023-03-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0038_menu_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="approved",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, null=True
            ),
        ),
    ]
