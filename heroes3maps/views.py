from rest_framework import generics, mixins, permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet

from heroes3maps.models import ActionHistory, Map
from heroes3maps.serializers import (
    ActionHistorySerializer,
    CreateActionHistorySerializer,
    CreateMapSerializer,
    MapSerializer,
    MapSerializerWithActions,
)
from progress_tracker.common import CustomSerializerMixin


class MapView(
    CustomSerializerMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_action_classes = {"default": MapSerializer, "create": CreateMapSerializer}
    lookup_field = "id"

    def get_queryset(self):
        return Map.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserActions(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActionHistorySerializer

    def get_queryset(self):
        return ActionHistory.objects.filter(user=self.request.user)


class MapsWithActions(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MapSerializerWithActions

    def get_queryset(self):
        return Map.objects.filter(user=self.request.user)


class UpdateMapStatus(CreateAPIView, mixins.CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateActionHistorySerializer

    def post(self, request, *args, **kwargs):
        request.data.update({"map": self.kwargs.get("id")})
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
