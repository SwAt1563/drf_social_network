
from django.urls import path, include
from account import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


app_name = 'account'
urlpatterns = [
        path('register/', views.RegisterUserAPIView.as_view(), name='register'),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]