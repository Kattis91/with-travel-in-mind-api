from django.contrib.auth.models import User
from .models import Explorer
from rest_framework import status
from rest_framework.test import APITestCase


class ExplorerListViewTests(APITestCase):
    def setUp(self):
        kattis = User.objects.create_user(username='kattis', password='pass1234')
        misha = User.objects.create_user(username='misha', password='pass1234')

    def test_profile_automatically_created_on_user_creation(self):
        response = self.client.get('/explorers/')
        count = Explorer.objects.count()
        self.assertEqual(count, 2)

    def test_can_list_explorers(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
