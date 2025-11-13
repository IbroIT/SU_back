from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AsNumbersViewSet,
    DetailStatisticsViewSet,
    FacultyViewSet, 
    AccreditationViewSet,
    LeadershipViewSet,
    QualityManagementSystemView,
    QualityPrincipleViewSet,
    QualityDocumentViewSet,
    QualityProcessGroupViewSet,
    QualityProcessViewSet,
    QualityStatisticViewSet,
    QualityAdvantageViewSet,
    QualitySettingsView,
    ProgramViewSet,
    ProgramDetailView,
    ResourceListView
)

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet, basename='hsm-faculty')
router.register(r'accreditations', AccreditationViewSet, basename='hsm-accreditations')
router.register(r'leadership', LeadershipViewSet, basename='hsm-leadership')

# Quality Management System routes
router.register(r'quality/principles', QualityPrincipleViewSet, basename='hsm-quality-principles')
router.register(r'quality/documents', QualityDocumentViewSet, basename='hsm-quality-documents')
router.register(r'quality/process-groups', QualityProcessGroupViewSet, basename='hsm-quality-process-groups')
router.register(r'quality/processes', QualityProcessViewSet, basename='hsm-quality-processes')
router.register(r'quality/statistics', QualityStatisticViewSet, basename='hsm-quality-statistics')
router.register(r'quality/advantages', QualityAdvantageViewSet, basename='hsm-quality-advantages')

urlpatterns = [
    path('hsm/', include(router.urls)),
    # Комплексное API для всей системы качества
    path('hsm/quality/system/', QualityManagementSystemView.as_view(), name='hsm-quality-system'),
    # Настройки системы качества
    path('hsm/quality/settings/', QualitySettingsView.as_view(), name='hsm-quality-settings'),
    path( 'hsm/programs/', ProgramViewSet.as_view(), name='hsm-programs' ),
    path( 'hsm/programs/<int:pk>/', ProgramDetailView.as_view(), name='hsm-program-detail' ),
    path('hsm/as-numbers/', AsNumbersViewSet.as_view(), name='hsm-as-numbers'),
    path('hsm/detail-statistics/', DetailStatisticsViewSet.as_view(), name='hsm-detail-statistics'),
    path('hsm/e-resources/',ResourceListView.as_view(), name='resource_list'),
]
