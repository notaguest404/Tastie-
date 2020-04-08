from django.db import models
from django.utils import timezone #to implement location timezone
from django.contrib.auth.models import User #User table inside django project
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If user is dele, all his posts should be deleted too

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) #return full path as string
