"""
api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('friends/', include('friends.urls', namespace='friends')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('stories/', include('stories.urls', namespace='stories')),
    path('user_profile/', include('user_profile.urls', namespace='user_profile')),
]

# for confirm the static paths
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)