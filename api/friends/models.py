from django.db import models
from django.conf import settings
from account.models import UserAccount
from .mangers import FriendRequestManger
from .mangers import FriendListManger


class FriendList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user')
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                     related_name='friends',
                                     on_delete=models.SET_DEFAULT)

    objects = FriendListManger()

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        if account not in self.friends.all():
            self.friends.add(account)
            self.save()

    def remove_friend(self, account):
        if account in self.friends.all():
            self.friends.remove(account)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
                                  , related_name='sent')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
                                , related_name='received')

    is_active = models.BooleanField(default=True, blank=True, null=True)

    objects = FriendRequestManger()

    def accept(self):
        sender = FriendList.objects.get(self.from_user)
        receiver = FriendList.objects.get(self.to_user)
        if sender and receiver:
            sender.add_friend(receiver)
            receiver.add_friend(sender)
            self.is_active = False
            self.save()

    def decline(self):
        self.is_active = False
        self.save()
