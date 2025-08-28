from django.db import models
from django.conf import settings
from lessons.models import TutoringSession

class Message(models.Model):
    session = models.ForeignKey(TutoringSession, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"Message from {self.sender} in {self.session_id}"

