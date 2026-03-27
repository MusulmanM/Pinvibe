from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewset, ProfileViewset



router = DefaultRouter()
router.register("users/", UserViewset)
router.register("profile/", ProfileViewset)


urlpatterns = [
    path("", include(router.urls)),
]







