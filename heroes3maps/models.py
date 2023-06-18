from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    CASCADE,
    BigAutoField,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
    Model,
    PositiveSmallIntegerField,
)


class Map(Model):
    id = BigAutoField(primary_key=True)
    user = ForeignKey(get_user_model(), on_delete=CASCADE, related_name="user_maps")
    name = CharField(max_length=128)
    heroes_version = IntegerField(validators=[MaxValueValidator(7), MinValueValidator(1)])

    class Meta:
        unique_together = ("user", "name", "heroes_version")

    def __str__(self):
        return f"{self.name} for heroes {self.heroes_version} (added by {self.user.username})"


class StatusEnum(IntegerChoices):
    CLEAR = 0, "Clear"
    STARTED = 1, "Started"
    ABORTED = 2, "Aborted"
    SOLVED = 3, "Completed"
    IGNORED = 4, "Ignored"


class ActionHistory(Model):
    map = ForeignKey(Map, on_delete=CASCADE, related_name="map_actions")
    user = ForeignKey(get_user_model(), on_delete=CASCADE, related_name="user_map_actions")
    status = PositiveSmallIntegerField(default=StatusEnum.CLEAR, choices=StatusEnum.choices)
    date = DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        date = self.date.strftime("%Y/%m/%d %H:%M:%S")
        return f"{self.user.username} - {self.map.name} - {self.get_status_display()} - {date}"
