# Generated by Django 4.2.2 on 2023-06-17 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("games", "0002_game_user_alter_actionhistory_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_games",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]