# Generated by Django 4.2.5 on 2024-03-19 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0002_alter_order_massage"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="pdf_file",
            field=models.FileField(default=1, upload_to="pdfs/"),
            preserve_default=False,
        ),
    ]
