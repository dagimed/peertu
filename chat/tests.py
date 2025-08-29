from subjects.models import Subject
from lessons.models import TutoringSession
from users.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone

class MessageTests(APITestCase):
    def setUp(self):
        # Create sender
        self.sender = User.objects.create_user(
            username="unique_sender5",
            email="unique_sender5@example.com",
            password="StrongPass!123",
            role="learner"
        )
        # Create recipient
        self.recipient = User.objects.create_user(
            username="unique_recipient5",
            email="unique_recipient5@example.com",
            password="StrongPass!321",
            role="tutor"
        )

        # Create a subject
        self.subject = Subject.objects.create(name="Mathematics")

        # Create a tutoring session
        self.session = TutoringSession.objects.create(
            tutor=self.recipient,
            learner=self.sender,
            subject=self.subject,
            start_time=timezone.now()
        )

        # Log in sender
        login_resp = self.client.post("/api/auth/login/", {
            "username": self.sender.username,
            "password": "StrongPass!123"
        }, format='json')
        self.token = login_resp.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_send_message(self):
        url = "/api/messages/"
        data = {
            "recipient": self.recipient.username,
            "content": "Hello, this is a test message!",
            "session": self.session.id
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code, getattr(response, 'data', response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
