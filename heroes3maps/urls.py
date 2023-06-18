from django.urls import path

from heroes3maps.views import MapsWithActions, MapView, UpdateMapStatus, UserActions

API_VERSION = "v1"

urlpatterns = [
    path(f"{API_VERSION}/maps-actions/", MapsWithActions.as_view()),
    path(f"{API_VERSION}/maps/", MapView.as_view({"get": "list", "post": "create"})),
    path(
        f"{API_VERSION}/maps/<int:id>/",
        MapView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path(f"{API_VERSION}/maps/<int:id>/status/", UpdateMapStatus.as_view()),
    path(f"{API_VERSION}/actions/", UserActions.as_view()),
]
