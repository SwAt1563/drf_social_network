from django.contrib import admin
from .models import Comment, Like, Unlike, Post
# Register your models here.

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Unlike)
admin.site.register(Like)
