from rest_framework.fields import DateTimeField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from heroes3maps.models import ActionHistory, Map


class MapSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = ("id", "name", "heroes_version")


class CreateMapSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Map
        fields = ("id", "name", "heroes_version", "user")


class CreateActionHistorySerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        fields = ("map", "user", "status", "date")


class ActionHistorySerializer(ModelSerializer):
    class Meta:
        model = ActionHistory
        fields = ("date", "status", "map_id")


class MapSerializerWithActions(ModelSerializer):
    map_actions = ActionHistorySerializer(many=True)

    class Meta:
        model = Map
        fields = ("id", "name", "heroes_version", "map_actions")
