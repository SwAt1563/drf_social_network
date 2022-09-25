from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    # for Deactivate Account
    # we should use is_active attribute

    def __str__(self):
        return self.username
