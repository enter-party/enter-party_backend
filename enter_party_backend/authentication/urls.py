
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from rest_framework_social_oauth2 import views
from .views import MyTokenObtainPairView

urlpatterns = [
    # path('auth/', views.TokenView.as_view(), name='auth'),
    path('token/', MyTokenObtainPairView.as_view(), name='obtain_token_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token')
]