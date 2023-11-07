from django.contrib.auth.models import User
from .models import Explorer
from rest_framework import status
from rest_framework.test import APITestCase


class ExplorerListViewTests(APITestCase):
    def setUp(self):
        kattis = User.objects.create_user(username='kattis', password='pass1234')
        misha = User.objects.create_user(username='misha', password='pass1234')

    def test_explorer_automatically_created_on_user_creation(self):
        response = self.client.get('/explorers/')
        count = Explorer.objects.count()
        self.assertEqual(count, 2)

    def test_can_list_explorers(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ExplorerDetailViewTests(APITestCase):
    def setUp(self):
        kattis = User.objects.create_user(username='kattis', password='pass1234')
        misha = User.objects.create_user(username='misha', password='pass1234')

    def test_can_retrieve_explorer_using_valid_id(self):
        response = self.client.get('/explorers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_explorer_using_invalid_id(self):
        response = self.client.get('/explorers/25/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_explorer_profile(self):
        self.client.login(username='kattis', password='pass1234')
        response = self.client.put('/explorers/1/', {'name': 'kattis svedmark'})
        explorer = Explorer.objects.filter(pk=1).first()
        self.assertEqual(explorer.name, 'kattis svedmark')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_update_other_explorers(self):
        self.client.login(username='misha', password='pass1234')
        response = self.client.put('/explorers/1/', {'name': 'kattis svedmark'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cannot_delete_own_explorer_profile(self):
        self.client.login(username='kattis', password='pass1234')
        response = self.client.delete('/explorers/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    