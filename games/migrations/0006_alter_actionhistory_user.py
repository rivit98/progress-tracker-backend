# Generated by Django 4.2.2 on 2023-06-18 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("games", "0005_alter_game_name_alter_game_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actionhistory",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_game_actions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]