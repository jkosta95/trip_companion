
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

REGISTER_USER_URL = reverse('register')
CREATE_USER_URL = reverse('login')
ME_URL = reverse('profile')



def create_user(**params):
    return get_user_model().objects.create_user(**params)

def sample_user(username, password):
    return get_user_model().objects.create_user(username, password)


class PublicUserApiTests(TestCase):
    """
        Test the users API (public)
    """
    def setUp(self):
        """ one client for our test suite that
            we can reuse for all of the tests
        """
        self.client = Client()

    def test_create_valid_user_success(self):

        """
            Test creating user with valid payload is successful.
            Payload - the object that you pass to the API when you
        """
        payload = {
            'username' : 'SomeUser',
            'email': 'test@kosta.com',
            'password' : 'test123',
            'first_name': 'Test name',
            'last_name' : 'Second name'
         }

         # make request
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, 200)

    def test_user_exists(self):

        """ Test creating users that already exists fails """
        payload = { 'username' : 'SomeUser', 'email':'test@kosta.com', 'password':'test123'}
        res =  sample_user(payload['username'], payload['password'])

        # make request
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, 200)
