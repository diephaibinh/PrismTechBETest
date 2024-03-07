from rest_framework.permissions import AllowAny
from rest_framework import generics

from apps.user_auth.api.serializers import UserRegisterSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = UserRegisterSerializer
