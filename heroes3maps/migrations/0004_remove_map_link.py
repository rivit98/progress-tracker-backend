# Generated by Django 4.1.6 on 2023-02-15 19:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("heroes3maps", "0003_alter_map_heroes_version"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="map",
            name="link",
        ),
    ]
