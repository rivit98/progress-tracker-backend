from django.urls import path

from user.views import CreateUserView, UserView

API_VERSION = 'v1'

urlpatterns = [
    path(f'{API_VERSION}/register/', CreateUserView.as_view()),
    path(f'{API_VERSION}/me/', UserView.as_view()),
]
