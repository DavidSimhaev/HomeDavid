# Generated by Django 4.1.5 on 2023-03-02 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0002_restaurant_categ"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("dish", models.CharField(max_length=30)),
                (
                    "image",
                    models.ImageField(max_length=255, null=True, upload_to="images/"),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "categ",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Food.category"
                    ),
                ),
            ],
        ),
    ]