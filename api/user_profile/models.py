from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=True)
    location = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='users_images/')

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        return reverse('user_profile:view', args=[self.slug])