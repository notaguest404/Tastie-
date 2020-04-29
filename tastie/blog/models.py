from django.db import models
from django.utils import timezone #to implement location timezone
from django.contrib.auth.models import User #User table inside django project
from django.urls import reverse
from django import forms
from taggit.managers import TaggableManager
from PIL import Image
from django.conf import settings


DIF_CHOICES =(
    ("1", "Easy"),
    ("2", "Intermediate"),
    ("3", "Advanced")
)

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

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) #return full path as string

    def save(self,*args, **kwargs): #change save method to resize image passed by the user
        super(Post, self).save(*args, **kwargs)

        img= Image.open(self.image.path) #open image of current instance

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path) #save resized image

class Like(models.Model):
    ''' like  comment '''

    post = models.OneToOneField(Post, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_post_likes')


class DisLike(models.Model):
    ''' Dislike  comment '''

    post = models.OneToOneField(Post, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_post_dis_likes')
