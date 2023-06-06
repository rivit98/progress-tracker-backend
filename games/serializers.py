from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer

from heroes3maps.models import ActionHistory, Map


class MapsSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"


class ActionHistorySerializerSave(ModelSerializer):
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        fields = "__all__"
