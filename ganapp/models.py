from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='photos')


class GeneratedImage(models.Model):
    input_image = models.ImageField(upload_to="input_images/")
    output_image = models.ImageField(upload_to="output_images/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"GeneratedImage {self.id}"

class UserImage(models.Model):
    image = models.ImageField(upload_to='original_images/')
    output_image = models.ImageField(upload_to='output_images/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_images')

