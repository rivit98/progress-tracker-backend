from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer

from crackmes.models import ActionHistory, ScrapperHistory, Task


class ActionHistorySerializerSave(ModelSerializer):
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        fields = "__all__"


class ActionHistorySerializer(ModelSerializer):
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        exclude = ("user", "task", "id")


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ("language",)

    def to_representation(self, instance):
        r = super().to_representation(instance)
        r["id"] = str(r["id"])
        return r


class ScrapperHistorySerializer(ModelSerializer):
    date = DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = ScrapperHistory
        exclude = ("id", "success")
