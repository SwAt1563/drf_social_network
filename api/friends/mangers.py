from .models import FriendRequest, FriendList
from account.models import UserAccount
from django.db import models


class FriendListManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_mutual_friends(self, user1, user2):
        friends1 = self.get_queryset().filter(user=user1).first().friends.all()
        friends2 = self.get_queryset().filter(user=user2).first().friends.all()
        return friends1.intersection(friends2)


class FriendRequestManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def clean(self):
        self.get_queryset().filter(is_active=False).delete()
