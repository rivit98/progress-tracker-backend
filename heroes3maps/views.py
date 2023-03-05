from collections import defaultdict

from rest_framework import generics, mixins, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from heroes3maps.models import ActionHistory, Map
from heroes3maps.permissions import HasSpecialProgressViewAccess, ReadOnly
from heroes3maps.serializers import ActionHistorySerializerSave, MapsSerializer


class MapsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = ((IsAuthenticated & HasSpecialProgressViewAccess) | ReadOnly,)
    serializer_class = MapsSerializer
    lookup_field = "id"
    queryset = Map.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MapView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    permission_classes = ((IsAuthenticated & HasSpecialProgressViewAccess) | ReadOnly,)
    serializer_class = MapsSerializer
    lookup_field = "id"
    queryset = Map.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserActions(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        queryset = ActionHistory.objects.filter(user=user)

        actions_dict = defaultdict(list)
        for action in queryset:
            actions_dict[str(action.map_id)].append({"date": action.date, "status": action.status})

        return Response(actions_dict)


class UpdateStatus(APIView):
    permission_classes = [permissions.IsAuthenticated]
    model = ActionHistory

    def post(self, request, id):
        serializer_data = {
            "map": id,
            "user": self.request.user.id,
            "status": request.data.get("status"),
        }
        serializer = ActionHistorySerializerSave(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
