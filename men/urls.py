from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenViewSet

router = DefaultRouter()
router.register(r'posts', MenViewSet, basename='men')

urlpatterns = [
    path('', include(router.urls)),
]
