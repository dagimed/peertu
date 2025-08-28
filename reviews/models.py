from django.db import models
from django.conf import settings
from lessons.models import TutoringSession

class Review(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_reviews")
    learner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="written_reviews")
    session = models.OneToOneField(TutoringSession, on_delete=models.CASCADE, related_name="review", null=True, blank=True)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = [("tutor", "learner")]  # a learner can rate a tutor once

    def __str__(self):
        return f"Review {self.rating} for {self.tutor} by {self.learner}"

