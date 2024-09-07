from django.urls import path, include
from rest_framework import routers

from cafe.views import ProductView

router = routers.DefaultRouter()
router.register("products", ProductView)

urlpatterns = [
    path("", include(router.urls)),
]
