# Generated by Django 4.2.2 on 2023-06-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("heroes3maps", "0004_remove_map_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="map",
            name="name",
            field=models.CharField(max_length=128),
        ),
    ]
