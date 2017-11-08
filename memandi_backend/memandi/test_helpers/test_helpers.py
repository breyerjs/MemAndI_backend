from django.test import TestCase
from rest_framework.test import APIClient
from memandi.models import User, Memory
from django.urls import reverse
from datetime import datetime

class TestHelper:
    def __init__(self):
        self.create_user_route = reverse('user')

        self.user_information = {
            'username': 'alobar',
            'email': 'panpanpan',
            'password': 'jitterbug@perfume.com',
            'first_name': 'Alobar',
            'last_name': 'Pan'
        }

        self.memory_information = {
            'text': 'Did a lot of writing today',
            'pub_date': str(datetime.now()),
            'starred': False,
            'user': None # added during usage
        }

    def create_user(self):
        return APIClient().post(self.create_user_route, data=self.user_information, format='json')

    def create_memory(self, user_id):
        self.memory_route = reverse('create_memory', kwargs={'user_id': user_id})
        body = self.memory_information
        body['user'] = user_id
        return APIClient().post(self.memory_route, data=body, format='json')
