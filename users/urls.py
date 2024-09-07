from django.urls import path, include

from users.views import CreateUser

urlpatterns = [
    path("registration/", CreateUser.as_view(), name="register_user"),
]
