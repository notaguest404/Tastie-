from django.contrib.auth.models import User #to send the signal from users
from django.db.models.signals import post_save #to trigger when object is saved
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #parameters: signal and receiver
def create_profile(sender, instance, created, **kwargs): #parameters passed by the signal
    if created:
        Profile.objects.create(user=instance) #create profile object

def save_profile(sender, instance, **kwargs): #parameters passed by the signal
    instance.profile.save() #save the object profile
