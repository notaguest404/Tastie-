from django.contrib import admin
from .models import Profile
from image_cropping import ImageCroppingMixin

class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
