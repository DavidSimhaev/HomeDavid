# Generated by Django 4.1.5 on 2023-02-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0047_remove_price_title_alter_price_approved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="approved",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
