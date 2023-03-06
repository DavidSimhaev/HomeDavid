# Generated by Django 4.1.5 on 2023-03-02 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("Food", "0011_restaurant_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="group",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="auth.group"
            ),
            preserve_default=False,
        ),
    ]