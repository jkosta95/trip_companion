from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # when the user is deleted we want to delete the profile as well
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
