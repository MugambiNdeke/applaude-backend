from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import TestRunViewSet

router = DefaultRouter()
router.register(r'tests', TestRunViewSet, basename='testrun')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls
    path('api/core/', include('core.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/', include(router.urls)),
]

 
