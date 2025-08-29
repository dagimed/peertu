from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            "username": "unique_user1",
            "email": "unique_user1@example.com",
            "password": "StrongPass@123"
        }
        response = self.client.post("/api/auth/register/", data, format="json")
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_login_jwt(self):
        # create a unique user first
        user = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            password='StrongPass456!',
            role='learner'
        )

        url = '/api/auth/login/'
        data = {
            'username': 'testuser2',
            'password': 'StrongPass456!'
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code, getattr(response, 'data', response.content))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)