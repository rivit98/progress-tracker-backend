from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.fields import ReadOnlyField, CharField, DateTimeField
from rest_framework.serializers import ModelSerializer

from crackmes.models import Task, ActionHistory


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class UserSerializer(ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    solved_count = ReadOnlyField()
    password = CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'solved_count', 'groups')


class ActionHistorySerializerSave(ModelSerializer):
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        fields = '__all__'


class ActionHistorySerializer(ModelSerializer):
    date = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = ActionHistory
        exclude = ('user', 'task', 'id')


class TaskSerializer(ModelSerializer):
    actions = ActionHistorySerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskSerializerAnonymous(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
