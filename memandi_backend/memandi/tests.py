from django.test import TestCase
from rest_framework.test import APIClient
from memandi.models import User, Memory
from django.urls import reverse
from .test_helpers.test_helpers import TestHelper

test_helper = TestHelper()

class TestSignup(TestCase):
    def setUp(self):
        self.USERNAME = test_helper.user_information.get('username')
        self.EMAIL = test_helper.user_information.get('email')

        self.api_client = APIClient()

    def test_can_create_user(self):
        response = test_helper.create_user()
        created_user = User.objects.filter(username=self.USERNAME).first()

        self.assertEquals(response.status_code, 201)
        self.assertEquals(created_user.email, self.EMAIL)

    def test_creating_same_user_twice_throws_exception(self):
        response1 = test_helper.create_user()
        response2 = test_helper.create_user()
        self.assertEquals(response2.status_code, 400)

class TestMemories(TestCase):
    def setUp(self):
        create_user_response = test_helper.create_user()
        self.user = User.objects.get(username=test_helper.user_information['username'])

    def test_can_add_one_memory(self):
        response = test_helper.create_memory(self.user.id)
        self.assertEquals(response.status_code, 201)

    def test_can_add_two_memories(self):
        response1 = test_helper.create_memory(self.user.id)
        response2 = test_helper.create_memory(self.user.id)
        self.assertEquals(response2.status_code, 201)
