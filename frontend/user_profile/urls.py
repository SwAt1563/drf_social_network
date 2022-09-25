from django.urls import path, include
from user_profile import views
app_name = 'user_profile'
urlpatterns = [
    path('<slug:slug>/', views.profile, name='user_profile'),
    path('edit/<slug:slug>', views.edit_profile, name='edit_profile'),
]