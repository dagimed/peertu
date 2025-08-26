from django.db import models
from django.conf import settings
from subjects.models import Subject

class TutorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_profile")
    bio = models.TextField(blank=True)
    availability_text = models.TextField(blank=True)
    subjects = models.ManyToManyField(Subject, related_name="tutors", blank=True)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return f"TutorProfile<{self.user.username}>"
