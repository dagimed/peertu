# tutors/urls.py
from rest_framework.routers import DefaultRouter
from .views import TutorProfileViewSet

router = DefaultRouter()
router.register(r"tutors", TutorProfileViewSet, basename="tutor")
urlpatterns = router.urls
