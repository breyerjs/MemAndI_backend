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

class TestLogin(TestCase):
    def setUp(self):
        create_user_response = test_helper.create_user()
        self.user = User.objects.get(username=test_helper.user_information['username'])

    def test_can_log_in(self):
        known_token = test_helper.get_user_token(self.user.username)
        client = APIClient()
        body = {
            'username': self.user.username,
            'password': self.user.password
        }
        response = client.post(test_helper.login_route, data=body, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['token'], str(known_token))

    def test_wrong_password_cant_log_in(self):
        pass

    def test_wrong_username_cant_log_in(self):
        pass

class TestMemories(TestCase):
    def setUp(self):
        create_user_response = test_helper.create_user()
        self.user = User.objects.get(username=test_helper.user_information['username'])

    """
        POST
    """

    def test_can_add_one_memory(self):
        response = test_helper.create_memory(self.user.id)
        memory_added = [m for m in Memory.objects.filter(text=test_helper.memory_information['text'])]

        self.assertEquals(len(memory_added), 1)
        self.assertEquals(response.status_code, 201)

    def test_can_add_two_memories(self):
        response1 = test_helper.create_memory(self.user.id)
        response2 = test_helper.create_memory(self.user.id)
        memories_added = [m for m in Memory.objects.filter(text=test_helper.memory_information['text'])]

        self.assertEquals(len(memories_added), 2)
        self.assertEquals(response2.status_code, 201)

    """
        GET
    """

    def test_can_get_all_memories(self):
        test_helper.create_memory(self.user.id)
        memories = test_helper.get_all_memories(self.user.id)

        self.assertEquals(len(memories.data), 1)
        self.assertEquals(memories.data[0]['text'], test_helper.memory_information['text'])

    def test_unauthenticated_user_gets_401(self):
        test_helper.create_user(test_helper.user_information)
        user = User.objects.get(username=test_helper.user_information['username'])
        unauthenticated_client = APIClient()
        memory_route = reverse('memory_create_list', kwargs={'user_id': self.user.id})
        response = unauthenticated_client.get(memory_route)
        self.assertEquals(401, response.status_code)

    def test_cant_get_different_users_memories(self):
        test_helper.create_memory(self.user.id)

        test_helper.create_user(test_helper.second_user_information)
        second_user = User.objects.get(username=test_helper.second_user_information['username'])
        second_user_client = test_helper.get_authenticated_client(second_user.username)
        first_user_memory_route = reverse('memory_create_list', kwargs={'user_id': self.user.id})
        response = second_user_client.get(first_user_memory_route)

        self.assertEquals(403, response.status_code)
