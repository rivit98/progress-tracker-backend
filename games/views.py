from rest_framework import generics, mixins, permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet

from games.models import ActionHistory, Game
from games.serializers import (
    ActionHistorySerializer,
    CreateActionHistorySerializer,
    CreateGameSerializer,
    GameSerializer,
    GameSerializerWithActions,
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

    def post(self, request, *args, **kwargs):
        request.data.update({"game": self.kwargs.get("id")})
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
