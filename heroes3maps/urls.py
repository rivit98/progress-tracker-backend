from django.urls import path

from heroes3maps.views import MapsView, MapView, UpdateStatus, UserActions

API_VERSION = "v1"

urlpatterns = [
    path(f"{API_VERSION}/maps/", MapsView.as_view()),
    path(f"{API_VERSION}/maps/<int:id>/", MapView.as_view()),
    path(f"{API_VERSION}/maps/<int:id>/status/", UpdateStatus.as_view()),
    path(f"{API_VERSION}/actions/", UserActions.as_view()),
]
