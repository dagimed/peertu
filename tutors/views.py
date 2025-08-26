from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import TutorProfile
from .serializers import TutorProfileSerializer

class TutorProfileViewSet(viewsets.ModelViewSet):
    queryset = TutorProfile.objects.select_related("user").prefetch_related("subjects")
    serializer_class = TutorProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["subjects"]     # filter by subject id: ?subjects=3
    search_fields = ["user__username", "bio", "availability_text"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
