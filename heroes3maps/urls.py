from django.urls import path

from heroes3maps.views import MapsView, MapView

API_VERSION = "v1"

urlpatterns = [
    path(f"{API_VERSION}/maps", MapsView.as_view()),
    path(f"{API_VERSION}/maps/<int:id>", MapView.as_view()),
]
