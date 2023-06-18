from django.urls import path

from games.views import GamesWithActions, GameView, UpdateGameStatus, UserActions

API_VERSION = "v1"

urlpatterns = [
    path(f"{API_VERSION}/games-actions/", GamesWithActions.as_view()),
    path(f"{API_VERSION}/games/", GameView.as_view({"get": "list", "post": "create"})),
    path(
        f"{API_VERSION}/games/<int:id>/",
        GameView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path(f"{API_VERSION}/games/<int:id>/status/", UpdateGameStatus.as_view()),
    path(f"{API_VERSION}/actions/", UserActions.as_view()),
]
