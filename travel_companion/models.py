from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Trip(models.Model):
    title = models.CharField(max_length=100)
    details =  models.TextField()
    point_of_destination = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'pk':self.pk})
