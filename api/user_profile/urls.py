from django.urls import path, include
from user_profile import views
app_name = 'user_profile'
urlpatterns = [
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile'),
]