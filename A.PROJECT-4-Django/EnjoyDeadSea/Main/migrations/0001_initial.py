# Generated by Django 4.2.5 on 2024-03-18 07:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("food", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["food"],
            },
        ),
        migrations.CreateModel(
            name="Massage",
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
                ("massage", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["massage"],
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("Date", models.DateField()),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=100)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "passport",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "count_people",
                    models.DecimalField(decimal_places=0, default=1, max_digits=10),
                ),
                (
                    "count_children",
                    models.IntegerField(
                        blank=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("boolweekends", models.BooleanField(null=True)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="Food",
                        to="Main.food",
                    ),
                ),
                (
                    "massage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="Massage",
                        to="Main.massage",
                    ),
                ),
            ],
            options={
                "ordering": ["food", "massage"],
            },
        ),
        migrations.CreateModel(
            name="ORDER_ID",
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
                ("indificator", models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("product", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "ORDER_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ORDER_ID",
                        to="Main.order_id",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="Main.order",
                    ),
                ),
            ],
        ),
    ]