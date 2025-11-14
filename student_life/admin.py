from django.contrib import admin
from .models import (
    PartnerOrganization, OrganizationSpecialization,
    InternshipRequirement, InternshipRequirementItem, ReportTemplate,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail,
    StudentAppeal, PhotoAlbum, Photo, VideoContent, StudentLifeStatistic,
    EResourceCategory, EResource, EResourceFeature, InstructionFiles, Exchange
)


# =============================================================================
# РЕГИСТРАЦИЯ МОДЕЛЕЙ ДЛЯ ПРАКТИКИ
# =============================================================================
admin.site.register(PartnerOrganization)
admin.site.register(OrganizationSpecialization)
admin.site.register(InternshipRequirement)
admin.site.register(InternshipRequirementItem)
admin.site.register(ReportTemplate)


# =============================================================================
# РЕГИСТРАЦИЯ МОДЕЛЕЙ ДЛЯ ИНСТРУКЦИЙ
# =============================================================================
admin.site.register(StudentGuide)
admin.site.register(GuideRequirement)
admin.site.register(GuideStep)
admin.site.register(GuideStepDetail)


# =============================================================================
# РЕГИСТРАЦИЯ МОДЕЛЕЙ ДЛЯ ОБРАЩЕНИЙ
# =============================================================================
admin.site.register(StudentAppeal)


# =============================================================================
# РЕГИСТРАЦИЯ МОДЕЛЕЙ ДЛЯ ФОТОГАЛЕРЕИ И ВИДЕО
# =============================================================================
admin.site.register(Photo)


# =============================================================================
# РЕГИСТРАЦИЯ МОДЕЛЕЙ ДЛЯ ЭЛЕКТРОННЫХ РЕСУРСОВ
# =============================================================================
admin.site.register(EResourceCategory)
admin.site.register(EResource)
admin.site.register(EResourceFeature)


# =============================================================================
# РЕГИСТРАЦИЯ МОДЕЛЕЙ ДЛЯ ФАЙЛОВ ИНСТРУКЦИЙ
# =============================================================================
admin.site.register(InstructionFiles)
admin.site.register(Exchange)