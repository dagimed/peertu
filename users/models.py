from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ("learner", "Learner"),
        ("tutor", "Tutor"),
        ("both", "Both"),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="learner")

    REQUIRED_FIELDS = ["email"]  

    def __str__(self):
        return f"{self.username} ({self.role})"
