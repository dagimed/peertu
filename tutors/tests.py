from rest_framework import status
from rest_framework.test import APITestCase

class TutorRegistrationTests(APITestCase):
    def test_register_tutor(self):
        url = "/api/auth/register/"
        data = {
            "username": "unique_tutor1",
            "email": "unique_tutor1@example.com",
            "password": "StrongPass!789",
            "role": "tutor"
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code, getattr(response, 'data', response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
