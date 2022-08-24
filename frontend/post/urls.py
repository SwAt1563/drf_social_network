from django.urls import path, include
from post import views
app_name = 'post'
urlpatterns = [
    path('', views.post, name='post'),
    path('edit', views.edit_post, name='edit_post'),

]