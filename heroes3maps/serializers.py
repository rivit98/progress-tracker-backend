from rest_framework.serializers import ModelSerializer

from heroes3maps.models import Map


class MapsSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"
