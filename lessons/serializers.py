from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TutoringSession
from subjects.serializers import SubjectSerializer
from subjects.models import Subject

User = get_user_model()

class TutoringSessionSerializer(serializers.ModelSerializer):
    tutor_username = serializers.CharField(source="tutor.username", read_only=True)
    learner_username = serializers.CharField(source="learner.username", read_only=True)
    subject_detail = SubjectSerializer(source="subject", read_only=True)

    class Meta:
        model = TutoringSession
        fields = [
            "id", "tutor", "tutor_username", "learner", "learner_username",
            "subject", "subject_detail", "start_time", "duration_minutes",
            "status", "created_at",
        ]
        read_only_fields = ["status", "created_at", "learner"]

    def validate(self, attrs):
        tutor = attrs.get("tutor")
        learner = self.context["request"].user
        if tutor == learner:
            raise serializers.ValidationError("Tutor and learner cannot be the same user.")
        return attrs

    def create(self, validated_data):
        # learner is always the requester
        validated_data["learner"] = self.context["request"].user
        return super().create(validated_data)
