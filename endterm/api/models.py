from django.db import models


# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True, default='')
    like_count = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
