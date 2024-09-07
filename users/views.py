from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from users.serializers import UserCreateSerializer


class CreateUser(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = get_user_model().objects.all()
