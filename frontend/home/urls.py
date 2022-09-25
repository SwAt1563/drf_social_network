from django.urls import path, include
from home import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('store_token/', views.store_token, name='store_token'),
]