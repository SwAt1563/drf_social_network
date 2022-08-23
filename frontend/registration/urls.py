from django.urls import path, include
from registration import views
app_name = 'registration'
urlpatterns = [
    path('', views.login, name='registration'),
]