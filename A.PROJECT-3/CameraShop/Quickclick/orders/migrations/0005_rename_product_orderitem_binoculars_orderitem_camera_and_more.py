# Generated by Django 4.2.5 on 2023-10-18 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0009_alter_profile_img_image"),
        ("orders", "0004_orderitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="product",
            new_name="Binoculars",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="Camera",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_item",
                to="Main.camera",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="lens",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_item",
                to="Main.lens",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="lightings",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_item",
                to="Main.lightings",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="tripods",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_item",
                to="Main.tripods",
            ),
        ),
    ]