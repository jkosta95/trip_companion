from django.test import TestCase
from django.contrib.auth import get_user_model

from travel_companion import models

def sample_user(username='kosta_user_name', password='testpass'):
    return get_user_model().objects.create_user(username, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        username = 'aleksandra'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'aleksandra',
            'test123test'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    def test_trip_str(self):
        """ Test the Trip string representation """
        recipe = models.Trip.objects.create(
            author= sample_user(),
            title = 'State of Alabama',
        )
        self.assertEqual(str(recipe), recipe.title)
