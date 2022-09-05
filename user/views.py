from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import AppUser
from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserView(APIView):
    model = get_user_model()
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user: AppUser = request.user
        oldPassword = request.data.get("oldPassword")
        newPassword = request.data.get("password")

        if not oldPassword:
            return Response(
                {"detail": "Missing oldPassword field"}, status=status.HTTP_400_BAD_REQUEST
            )

        if not newPassword:
            return Response(
                {"detail": "Missing password field"}, status=status.HTTP_400_BAD_REQUEST
            )

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
