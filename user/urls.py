from user.views import UserViewSet
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register(r"users", UserViewSet, basename="user")

urlpatterns = user_router.urls
