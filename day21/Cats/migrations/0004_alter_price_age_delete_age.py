# Generated by Django 4.1.5 on 2023-02-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0003_remove_price_temperament_breed_temperament_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="age",
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.DeleteModel(
            name="Age",
        ),
    ]
