from rest_framework.routers import DefaultRouter
from .views import TutoringSessionViewSet

router = DefaultRouter()
router.register(r"sessions", TutoringSessionViewSet, basename="session")
urlpatterns = router.urls
