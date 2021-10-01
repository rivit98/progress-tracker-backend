from collections import defaultdict
from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from crackmes.models import Task, AppUser, ActionHistory, ScrapperHistory
from crackmes.serializers import UserSerializer, TaskSerializer, ActionHistorySerializer, \
     ActionHistorySerializerSave, ScrapperHistorySerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserView(APIView):
    model = get_user_model()
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user: AppUser = request.user
        oldPassword = request.data.get('oldPassword')
        newPassword = request.data.get('password')

        if not oldPassword:
            return Response({"detail": "Missing oldPassword field"}, status=status.HTTP_400_BAD_REQUEST)

        if not newPassword:
            return Response({"detail": "Missing password field"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(oldPassword):
            return Response({"oldPassword": "Invalid password"}, status=status.HTTP_403_FORBIDDEN)

        user.set_password(newPassword)
        user.save()

        return Response(UserSerializer(request.user).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def delete(self, request):
        user: AppUser = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TasksView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class UpdateStatus(APIView):
    permission_classes = [permissions.IsAuthenticated]
    model = ActionHistory

    def post(self, request, id):
        serializer_data = {"task": id, "user": self.request.user.id, "status": request.data.get('status')}
        serializer = ActionHistorySerializerSave(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LastUpdated(RetrieveAPIView):
    serializer_class = ScrapperHistorySerializer
    model = ScrapperHistory

    def get_object(self):
        return ScrapperHistory.objects.all().filter(success=True).latest('date')


class HasSpecialProgressViewAccess(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='special_progress_view').exists()


class UserActions(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        queryset = ActionHistory.objects.filter(user=user)

        actionsDict = defaultdict(list)
        for action in queryset:
            actionsDict[str(action.task_id)].append({'date': action.date, 'status': action.status})

        return Response(actionsDict)

