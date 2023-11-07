from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='kattis', password='pass1234')

    def test_can_list_posts(self):
        kattis = User.objects.get(username='kattis')
        Post.objects.create(owner=kattis, title='My test post')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='kattis', password='pass1234')
        response = self.client.post('/posts/', {'title': 'My test post'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'My test post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        kattis = User.objects.create_user(
            username='kattis', password='pass1234')
        misha = User.objects.create_user(username='misha', password='pass1234')
        Post.objects.create(
            owner=kattis,
            title='My test post',
            description='kattis first post'
        )
        Post.objects.create(
            owner=misha,
            title='My first post',
            description='mishas first post'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'My test post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/25/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_post(self):
        self.client.login(username='kattis', password='pass1234')
        response = self.client.put('/posts/1/', {'title': 'My new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'My new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_update_others_post(self):
        self.client.login(username='misha', password='pass1234')
        response = self.client.put('/posts/1/', {'title': 'My new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_update_any_posts(self):
        response = self.client.put('/posts/1/', {'title': 'My new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_delete_own_post(self):
        self.client.login(username='kattis', password='pass1234')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_in_user_cannot_delete_others_post(self):
        self.client.login(username='misha', password='pass1234')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_delete_any_posts(self):
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
