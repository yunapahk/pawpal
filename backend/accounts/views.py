from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers import SignupSerializer, LoginSerializer, UserSerializer

class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token_info = serializer.save()
            return Response(token_info, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_204_NO_CONTENT)

class ToggleSuperuserStatus(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(pk=user_id)
            user.is_superuser = not user.is_superuser
            user.save()
            status_msg = "now" if user.is_superuser else "no longer"
            return Response({"message": f"User {user.username} is {status_msg} a superuser."})
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
