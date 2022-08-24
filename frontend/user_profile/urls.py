from django.urls import path, include
from user_profile import views
app_name = 'user_profile'
urlpatterns = [
    path('', views.profile, name='user_profile'),
    path('edit', views.edit_profile, name='edit_profile'),
]