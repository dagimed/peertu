from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Message
from .serializers import MessageSerializer
from lessons.models import TutoringSession

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        session_id = self.request.query_params.get("session")
        qs = Message.objects.select_related("sender", "session")
        if not session_id:
            return qs.none()
        # Only allow participants to view
        session = TutoringSession.objects.get(pk=session_id)
        if self.request.user not in [session.tutor, session.learner]:
            raise PermissionDenied("Not a participant of this session.")
        return qs.filter(session=session)

    def perform_create(self, serializer):
        session = serializer.validated_data["session"]
        if self.request.user not in [session.tutor, session.learner]:
            raise PermissionDenied("Not a participant of this session.")
        serializer.save(sender=self.request.user)