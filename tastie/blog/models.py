from django.db import models
from django.utils import timezone #to implement location timezone
from django.contrib.auth.models import User #User table inside django project
from django.urls import reverse
from .forms import DIF_CHOICES
from django import forms
from taggit.managers import TaggableManager
from PIL import Image

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200, default='Small Description')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If user is deleted, all his posts should be deleted too
    image = models.ImageField(default='defaultPost.jpg', upload_to='post_pics')
    difficulty = models.CharField(max_length=40, choices = DIF_CHOICES, default = DIF_CHOICES[1])
    duration = models.CharField(max_length=5, default= '00:30')
    method = models.TextField(default='Method')
    servings = models.CharField(max_length=2, default= '4')
    ingredients = models.TextField(default='Ingredients')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) #return full path as string

    def save(self,*args, **kwargs): #change save method to resize image passed by the user
        super(Post, self).save(*args, **kwargs)

        img= Image.open(self.image.path) #open image of current instance

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path) #save resized image
