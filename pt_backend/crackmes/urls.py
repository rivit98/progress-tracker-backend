from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from crackmes.views import CreateUserView, TasksView, UpdateStatus, UserView, LastUpdated, UserActions

API_VERSION = 'v1'

urlpatterns = [
    path(f'{API_VERSION}/auth/login/', TokenObtainPairView.as_view()),
    path(f'{API_VERSION}/auth/refresh/', TokenRefreshView.as_view()),
    path(f'{API_VERSION}/auth/register/', CreateUserView.as_view()),
    path(f'{API_VERSION}/users/me/', UserView.as_view()),


    path(f'{API_VERSION}/tasks/', TasksView.as_view()),
    path(f'{API_VERSION}/tasks/<int:id>/status/', UpdateStatus.as_view()),
    path(f'{API_VERSION}/tasks/lastUpdated/', LastUpdated.as_view()),
    path(f'{API_VERSION}/tasks/actions/', UserActions.as_view())
]
