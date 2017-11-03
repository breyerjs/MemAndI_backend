from django.test import TestCase
from rest_framework.test import APIRequestFactory
from memandi.models import User
from memandi.views import create_user

class TestSignup(TestCase):
    def setUp(self):
        self.USERNAME = 'alobar'
        self.PASSWORD = 'panpanpan'
        self.EMAIL = 'jitterbug@perfume.com'

        self.create_user_request_body = {
            'username': self.USERNAME,
            'email': self.EMAIL,
            'password': self.PASSWORD,
            'first_name': 'Alobar',
            'last_name': 'Pan',
        }

        self.factory = APIRequestFactory()

    def test_can_create_user(self):
        body = self.create_user_request_body
        request = self.factory.post("/users/create", data=body, format='json')
        response = create_user(request)
        created_user = User.objects.filter(username=self.USERNAME).first()

        self.assertEquals(response.status_code, 204)
        self.assertEquals(created_user.email, self.EMAIL)

    def test_creating_same_user_twice_returns_400(self):
        body = self.create_user_request_body
        request = self.factory.post("/users/create", data=body, format='json')
        response1 = create_user(request)
        response2 = create_user(request)

        self.assertEquals(response2.status_code, 400)
