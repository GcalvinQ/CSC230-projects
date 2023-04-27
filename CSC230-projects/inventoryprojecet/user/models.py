from django.db import models
from django.contrib.auth.models import User
from user.permissions import UserPermsissions

# Create your models here.


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    image = models.ImageField(default='avatar.jpg',
                              upload_to='profile_images')
    
    class Meta:
        permissions = [
            ('trained', 'Trained'),
            ('worker', 'Student Worker')
        ]

    def __str__(self):
        return f'{self.staff.username}-Profile'