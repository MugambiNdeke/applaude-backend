from django.urls import path
from .views import RegisterView, LoginView, GitHubConnectView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('github/connect/', GitHubConnectView.as_view(), name='github_connect'),
]
