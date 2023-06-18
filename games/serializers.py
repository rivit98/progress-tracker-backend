from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from games.models import ActionHistory, Game


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "name")


class CreateGameSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Game
        fields = ("id", "name", "user")


class CreateActionHistorySerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        fields = ("game", "user", "status", "date")


class ActionHistorySerializer(ModelSerializer):
    class Meta:
        model = ActionHistory
        fields = ("date", "status", "game_id")


class GameSerializerWithActions(ModelSerializer):
    game_actions = ActionHistorySerializer(many=True)

    class Meta:
        model = Game
        fields = ("id", "name", "game_actions")
