from django.db import models
from django.conf import settings
# Create your models here.


class Story(models.Model):
    image = models.ImageField(upload_to='stories/')
    text = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def get_url(self):
        return self.image.url


