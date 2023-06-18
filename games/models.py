from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    BigAutoField,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerChoices,
    Model,
    PositiveSmallIntegerField,
)


class Game(Model):
    id = BigAutoField(primary_key=True)
    user = ForeignKey(get_user_model(), on_delete=CASCADE, related_name="user_games")
    name = CharField(max_length=256)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return f"{self.name} (added by {self.user.username})"


class StatusEnum(IntegerChoices):
    CLEAR = 0, "Clear"
    STARTED = 1, "Started"
    ABORTED = 2, "Aborted"
    SOLVED = 3, "Completed"
    IGNORED = 4, "Ignored"


class ActionHistory(Model):
    game = ForeignKey(Game, on_delete=CASCADE, related_name="game_actions")
    user = ForeignKey(get_user_model(), on_delete=CASCADE, related_name="user_game_actions")
    status = PositiveSmallIntegerField(default=StatusEnum.CLEAR, choices=StatusEnum.choices)
    date = DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        date = self.date.strftime("%Y/%m/%d %H:%M:%S")
        return f"{self.user.username} - {self.game.name} - {self.get_status_display()} - {date}"
