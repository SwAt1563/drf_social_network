from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    # for Deactivate Account
    status = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.username
