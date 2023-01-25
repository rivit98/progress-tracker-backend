from rest_framework import generics, mixins

from heroes3maps.models import Map
from heroes3maps.serializers import MapsSerializer


class MapsView(generics.ListAPIView):
    serializer_class = MapsSerializer
    queryset = Map.objects.all()


class MapView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
):
    serializer_class = MapsSerializer
    lookup_field = "id"
    queryset = Map.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
