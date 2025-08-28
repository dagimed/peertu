from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # list reviews of a tutor using ?tutor=<id>
        tutor_id = self.request.query_params.get("tutor")
        qs = Review.objects.select_related("tutor", "learner")
        return qs.filter(tutor_id=tutor_id) if tutor_id else qs.none()