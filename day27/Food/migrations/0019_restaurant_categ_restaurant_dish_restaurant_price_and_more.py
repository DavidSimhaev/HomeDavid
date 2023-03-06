# Generated by Django 4.1.5 on 2023-03-04 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0018_remove_menu_group_remove_menu_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="categ",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Food.category",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="dish",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.DeleteModel(
            name="Menu",
        ),
    ]