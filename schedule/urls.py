from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleSubsectionViewSet

router = DefaultRouter()
router.register(r'subsections', ScheduleSubsectionViewSet, basename='schedule-subsection')

urlpatterns = [
    path('', include(router.urls)),
]
