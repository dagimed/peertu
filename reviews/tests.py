from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from lessons.models import TutoringSession
from subjects.models import Subject

User = get_user_model()

class ReviewTests(APITestCase):
    def setUp(self):
        # Create tutor and learner users
        self.tutor = User.objects.create_user(
            username="tutor_review1",
            email="tutor_review1@example.com",
            password="StrongPass!101",
            role="tutor"
        )
        self.learner = User.objects.create_user(
            username="learner_review1",
            email="learner_review1@example.com",
            password="StrongPass!102",
            role="learner"
        )

        
        self.subject = Subject.objects.create(name="Physics")

        
        self.session = TutoringSession.objects.create(
            tutor=self.tutor,
            learner=self.learner,
            subject=self.subject,
            start_time="2025-09-01T10:00:00Z"  
        )

        # Login learner 
        login_url = '/api/auth/login/'
        login_data = {"username": "learner_review1", "password": "StrongPass!102"}
        response = self.client.post(login_url, login_data, format='json')
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Review payload
        self.review_data = {
            "tutor": self.tutor.id,
            "session": self.session.id,
            "rating": 5,
            "comment": "Excellent session!"
        }

    def test_create_review(self):
        url = '/api/reviews/'
        response = self.client.post(url, self.review_data, format='json')
        print(response.status_code, getattr(response, 'data', response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
