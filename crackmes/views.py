from collections import defaultdict
from datetime import datetime

from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from crackmes.models import ActionHistory, ScrapperHistory, Task
from crackmes.serializers import (
    ActionHistorySerializerSave,
    ScrapperHistorySerializer,
    TaskSerializer,
)


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
        try:
            return ScrapperHistory.objects.all().filter(success=True).latest('date')
        except ScrapperHistory.DoesNotExist:
            return ScrapperHistory(date=datetime.utcfromtimestamp(0))


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
