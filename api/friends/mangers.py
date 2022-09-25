from account.models import UserAccount
from django.db import models


class FriendListManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_mutual_friends(self, user1, user2):
        friends1 = self.get_queryset().get(user=user1).friends.all()
        friends2 = self.get_queryset().get(user=user2).friends.all()
        return friends1.intersection(friends2).difference(UserAccount.objects.filter(pk__in=(user1.id, user2.id)))


class FriendRequestManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def clean(self):
        self.get_queryset().filter(is_active=False).delete()
