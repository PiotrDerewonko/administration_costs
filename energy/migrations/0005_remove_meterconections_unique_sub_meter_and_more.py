# Generated by Django 4.1.1 on 2023-01-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("energy", "0004_meterconections_unique_sub_meter"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="meterconections", name="unique_sub_meter",
        ),
        migrations.AddConstraint(
            model_name="meterconections",
            constraint=models.UniqueConstraint(
                fields=("sub_meter",),
                name="unique_sub_meter",
                violation_error_message="Podany licznik był już użyty jako podlicznik. Sprawdź schemat",
            ),
        ),
    ]
