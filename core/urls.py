from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestRunViewSet

router = DefaultRouter()
router.register(r'tests', TestRunViewSet, basename='testrun')

urlpatterns = [
    path('', include(router.urls)),
]
