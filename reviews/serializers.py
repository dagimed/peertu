from rest_framework import serializers
from django.db.models import Avg
from .models import Review
from tutors.models import TutorProfile

class ReviewSerializer(serializers.ModelSerializer):
    tutor_username = serializers.CharField(source="tutor.username", read_only=True)
    learner_username = serializers.CharField(source="learner.username", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "tutor", "tutor_username", "learner", "learner_username", "session", "rating", "comment", "created_at"]
        read_only_fields = ["learner", "created_at"]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        validated_data["learner"] = self.context["request"].user
        review = super().create(validated_data)

        # Update tutor avg rating
        tutor = review.tutor
        avg = Review.objects.filter(tutor=tutor).aggregate(a=Avg("rating"))["a"] or 0
        profile, _ = TutorProfile.objects.get_or_create(user=tutor)
        profile.avg_rating = round(avg, 2)
        profile.save()

        return review
