from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TutoringSession
from .serializers import TutoringSessionSerializer
from django.db.models import Q


class TutoringSessionViewSet(viewsets.ModelViewSet):
    serializer_class = TutoringSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TutoringSession.objects.filter(
            Q(tutor=user) | Q(learner=user)
        ).select_related("tutor", "learner", "subject")

    @action(detail=True, methods=["patch"], url_path="set-status")
    def set_status(self, request, pk=None):
        session = self.get_object()
        new_status = request.data.get("status")
        if session.tutor != request.user:
            return Response({"detail": "Only the tutor can change status."}, status=403)
        if new_status not in dict(TutoringSession.STATUS_CHOICES):
            return Response({"detail": "Invalid status."}, status=400)
        session.status = new_status
        session.save()
        return Response(self.get_serializer(session).data)

