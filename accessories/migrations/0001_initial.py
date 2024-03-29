# Generated by Django 5.0.2 on 2024-02-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accessory",
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
                (
                    "accessory_name",
                    models.CharField(
                        choices=[
                            ("casque", "Casque"),
                            ("Cockpit", "Cockpit"),
                            ("X", "X"),
                            ("Y", "Y"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
