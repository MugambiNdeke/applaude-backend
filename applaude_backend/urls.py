from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import TestRunViewSet

router = DefaultRouter()
router.register(r'tests', TestRunViewSet, basename='testrun')

urlpatterns = [
    path('admin/', admin.site.urls),
    # The error was on this line:
    path('api/auth/', include('users.urls')), 
    path('api/payments/', include('payments.urls')),
    path('api/', include(router.urls)),
]
