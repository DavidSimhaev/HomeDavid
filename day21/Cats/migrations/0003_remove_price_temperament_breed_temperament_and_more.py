# Generated by Django 4.1.5 on 2023-02-09 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0002_alter_breed_breed"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="temperament",
        ),
        migrations.AddField(
            model_name="breed",
            name="temperament",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="Cats.temperament",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="age",
            name="age",
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name="color",
            name="color",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="temperament",
            name="temperament",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
