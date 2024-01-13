from django.urls import path, include
from rest_framework import routers

from .views import (
    PersonViewSet,
    TeamViewSet,
)


router = routers.DefaultRouter()
router.register("teams", TeamViewSet)
router.register("people", PersonViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "team"
