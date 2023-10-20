# Generated by Django 4.2.5 on 2023-10-10 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0003_lens_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lens",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="category",
                to="Main.category",
            ),
        ),
    ]