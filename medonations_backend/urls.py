# medonations_backend/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogsViewSet

router = DefaultRouter()
router.register(r'blogs', BlogsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
