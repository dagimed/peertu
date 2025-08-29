from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()

class SubjectTests(APITestCase):
    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username="admin_user2",
            email="admin_user2@example.com",
            password="StrongPass!456"
        )

        # Obtain JWT token for admin
        url = reverse("token_obtain_pair")  
        response = self.client.post(url, {"username": "admin_user2", "password": "StrongPass!456"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data["access"]

        
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        
        self.subject_data = {
            "name": "Physics",
            "description": "Learn Physics from basics to advanced"
        }

    def test_create_subject(self):
        url = reverse("subject-list")  
        response = self.client.post(url, self.subject_data, format='json')
        print(response.status_code, getattr(response, 'data', response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
