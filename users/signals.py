'''
    post_save signal which gets fired after an object is saved
    - in this case post_save singal gets fired when the user is created
    - User model is the sender - sending the signal
    - receiver is going to be function

    We want User Profile to be created for each new User
'''
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
