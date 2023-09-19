# Generated by Django 4.2.5 on 2023-09-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0004_lightings_time_power"),
    ]

    operations = [
        migrations.CreateModel(
            name="Binoculars",
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
                ("name", models.CharField(db_index=True, max_length=30)),
                ("material", models.CharField(db_index=True, max_length=30)),
                ("range", models.CharField(db_index=True, max_length=30)),
                ("content", models.TextField(blank=True, max_length=3000)),
                ("image", models.ImageField(blank=True, upload_to="products/%Y/%m/%d")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_published", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="lightings",
            name="name",
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="tripods",
            name="name",
            field=models.CharField(db_index=True, max_length=10),
        ),
    ]