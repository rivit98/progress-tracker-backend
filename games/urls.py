from django.urls import path

from games.views import GamesView, GameView, UpdateStatus, UserActions

API_VERSION = "v1"

urlpatterns = [
    path(f"{API_VERSION}/games/", GamesView.as_view()),
    path(f"{API_VERSION}/games/<int:id>/", GameView.as_view()),
    path(f"{API_VERSION}/games/<int:id>/status/", UpdateStatus.as_view()),
    path(f"{API_VERSION}/actions/", UserActions.as_view()),
]
