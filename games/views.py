from rest_framework import generics, mixins, permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet

from games.models import ActionHistory, Game
from games.serializers import (
    CreateActionHistorySerializer,
    CreateGameSerializer,
    GameSerializer,
    GameSerializerWithActions, ActionHistorySerializer,
)
from progress_tracker.common import CustomSerializerMixin


class GameView(
    CustomSerializerMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_action_classes = {"default": GameSerializer, "create": CreateGameSerializer}
    lookup_field = "id"

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserActions(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActionHistorySerializer

    def get_queryset(self):
        return ActionHistory.objects.filter(user=self.request.user)


class GamesWithActions(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GameSerializerWithActions

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)


class UpdateGameStatus(CreateAPIView, mixins.CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateActionHistorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        kwargs["data"] = {**self.request.data, "game": self.kwargs.get("id")}
        return serializer_class(*args, **kwargs)
