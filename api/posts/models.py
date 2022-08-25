from django.db import models
from django.conf import settings
from autoslug import AutoSlugField

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    post = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.user.username} comment : on {self.post.user.username} post'


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.username} like : on {self.post.user.username} post'

    
class Unlike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE, related_name='unlikes')

    def __str__(self):
        return f'{self.user.username} unlike : on {self.post.user.username} post'


class Post(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    slug = AutoSlugField(unique=True, populate_from='user.username')


    def __str__(self):
        return self.text
