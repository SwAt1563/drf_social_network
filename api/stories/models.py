from django.db import models

# Create your models here.


class Story(models.Model):
    image = models.ImageField(upload_to='stories/')
    text = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return self.image.url


