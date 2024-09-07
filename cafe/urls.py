from django.urls import path, include
from rest_framework import routers

from cafe.views import ProductView, OrderView

router = routers.DefaultRouter()
router.register("products", ProductView)

urlpatterns = [
    path("", include(router.urls)),
    path("orders/", OrderView.as_view(), name="orders"),
]
