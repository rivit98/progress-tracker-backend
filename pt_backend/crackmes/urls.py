from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from crackmes.views import CreateUserView, TasksView, TaskView, UpdateStatus, UserView

urlpatterns = [
    path('api/v1/auth/login/', TokenObtainPairView.as_view()),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view()),
    path('api/v1/auth/register/', CreateUserView.as_view()),

    path('api/v1/users/me/', UserView.as_view()),

    path('api/v1/tasks/', TasksView.as_view()),
    path('api/v1/tasks/<int:id>/', TaskView.as_view()),
    path('api/v1/tasks/<int:id>/status', UpdateStatus.as_view()),
]
