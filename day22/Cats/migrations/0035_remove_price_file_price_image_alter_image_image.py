# Generated by Django 4.1.5 on 2023-02-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0034_alter_image_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="file",
        ),
        migrations.AddField(
            model_name="price",
            name="image",
            field=models.ImageField(max_length=255, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(max_length=255, null=True, upload_to="images/"),
        ),
    ]
