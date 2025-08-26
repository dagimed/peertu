from rest_framework import serializers
from .models import TutorProfile
from subjects.serializers import SubjectSerializer

class TutorProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    role = serializers.CharField(source="user.role", read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    subject_ids = serializers.PrimaryKeyRelatedField(
        source="subjects", queryset=__import__("subjects").subjects.models.Subject.objects.all(),
        many=True, write_only=True, required=False
    )

    class Meta:
        model = TutorProfile
        fields = ["id", "username", "role", "bio", "availability_text", "avg_rating", "subjects", "subject_ids"]
