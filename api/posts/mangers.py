from django.db import models
from .models import Like, Unlike


class PostManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def add_like(self, user, post):
        # if there unlike then delete it before make like
        unlike = Unlike.objects.get(user=user, post=post)
        if unlike:
            unlike.delete()
        like, _ = Like.objects.get_or_create(user=user, post=post)

    def add_unlike(self, user, post):
        # if there like then delete it before make unlike
        like = Unlike.objects.get(user=user, post=post)
        if like:
            like.delete()
        unlike, _ = Unlike.objects.get_or_create(user=user, post=post)
