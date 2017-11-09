from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from memandi.models import User, Memory
from django.urls import reverse
from datetime import datetime

class TestHelper:
    def __init__(self):
        self.create_user_route = reverse('user_create_list')
        self.get_auth_token_route = reverse('get_auth_token')

        self.user_information = {
            'username': 'alobar',
            'email': 'jitterbug@perfume.com',
            'password': 'panpanpan',
            'first_name': 'Alobar',
            'last_name': 'Pan'
        }

        self.second_user_information = {
            'username': 'alobar',
            'email': 'jitterbug@perfume.com',
            'password': 'panpanpan',
            'first_name': 'Alobar',
            'last_name': 'Pan'
        }

        self.memory_information = {
            'text': 'Did a lot of writing today',
            'pub_date': str(datetime.now()),
            'starred': False,
            'user': None # added during usage
        }

    def create_user(self, data=None):
        if data is None:
            data = self.user_information
        return APIClient().post(self.create_user_route, data=data, format='json')

    # note: posting {username:username, password:password}
    # to the auth route should return the token, too
    # this can be sent like: http GET 127.0.0.1:8000/route 'Authorization: Token <token_value>'
    def get_authenticated_client(self, username='alobar'):
        token = Token.objects.get(user__username=username)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        return client

    def create_memory(self, user_id):
        memory_route = reverse('memory_create_list', kwargs={'user_id': user_id})
        body = self.memory_information
        body['user'] = user_id
        client = self.get_authenticated_client()
        return client.post(memory_route, data=body, format='json')

    def get_all_memories(self, user_id):
        memory_route = reverse('memory_create_list', kwargs={'user_id': user_id})
        client = self.get_authenticated_client()
        return client.get(memory_route)
