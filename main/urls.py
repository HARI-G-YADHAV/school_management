from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubjectViewSet, MarkViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'marks', MarkViewSet)

urlpatterns = router.urls