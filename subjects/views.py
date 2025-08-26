from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
