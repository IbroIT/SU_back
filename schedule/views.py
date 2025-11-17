from rest_framework import viewsets
from .models import ScheduleSubsection
from .serializers import ScheduleSubsectionSerializer

class ScheduleSubsectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScheduleSubsection.objects.filter(is_active=True).order_by('order')
    serializer_class = ScheduleSubsectionSerializer
