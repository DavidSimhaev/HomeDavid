# Generated by Django 4.1.5 on 2023-01-30 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("FinancesApp", "0004_rename_entr_ent_alter_ent_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Ent",
            new_name="Entry",
        ),
        migrations.AlterModelOptions(
            name="entry",
            options={"verbose_name_plural": "entries"},
        ),
    ]
