# Generated by Django 5.0.2 on 2024-02-19 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("career", "0006_alter_joboffer_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="joboffer", old_name="details", new_name="Details",
        ),
    ]
