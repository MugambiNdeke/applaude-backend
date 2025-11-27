from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import TestRunViewSet

router = DefaultRouter()
router.register(r'tests', TestRunViewSet, basename='testrun')

urlpatterns = [
    path('admin/', admin.site.urls),
    # The fix: Ensure both quotes and parenthesis are present
    path('api/auth/', include('users.urls')),
    path('api/auth/', include('users.urls')), 
    path('api/payments/', include('payments.urls')),
    path('api/', include(router.urls)),
]
