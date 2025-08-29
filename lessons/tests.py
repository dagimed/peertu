from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from lessons.models import TutoringSession
from subjects.models import Subject

User = get_user_model()

class TutoringSessionTests(APITestCase):
    def setUp(self):
        # Create tutor and learner
        self.tutor = User.objects.create_user(
            username="tutor_lesson1",
            email="tutor_lesson1@example.com",
            password="StrongPass!201",
            role="tutor"
        )
        self.learner = User.objects.create_user(
            username="learner_lesson1",
            email="learner_lesson1@example.com",
            password="StrongPass!202",
            role="learner"
        )

        # Create a subject
        self.subject = Subject.objects.create(name="Mathematics")

        # Login learner to get JWT token
        login_url = '/api/auth/login/'  
        login_data = {"username": "learner_lesson1", "password": "StrongPass!202"}
        response = self.client.post(login_url, login_data, format='json')
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Tutoring session payload
        self.session_data = {
            "tutor": self.tutor.id,
            "learner": self.learner.id,
            "subject": self.subject.id,
            "start_time": "2025-09-01T15:00:00Z"
        }

    def test_create_tutoring_session(self):
        url =  '/api/sessions/'
        response = self.client.post(url, self.session_data, format='json')
        print(response.status_code, getattr(response, 'data', response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
