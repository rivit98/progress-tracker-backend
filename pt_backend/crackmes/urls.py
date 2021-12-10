from django.urls import path

from crackmes.views import TasksView, UpdateStatus, LastUpdated, UserActions

API_VERSION = 'v1'

urlpatterns = [
    path(f'{API_VERSION}/', TasksView.as_view()),
    path(f'{API_VERSION}/<int:id>/status/', UpdateStatus.as_view()),
    path(f'{API_VERSION}/lastUpdated/', LastUpdated.as_view()),
    path(f'{API_VERSION}/actions/', UserActions.as_view())
]
