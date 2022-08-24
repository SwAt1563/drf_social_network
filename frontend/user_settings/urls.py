from django.urls import path, include
from user_settings import views
app_name = 'user_settings'
urlpatterns = [
    path('', views.settings, name='settings'),
]