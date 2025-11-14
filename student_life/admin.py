from django.contrib import admin
from .models import (
    PartnerOrganization, OrganizationSpecialization,
    InternshipRequirement, InternshipRequirementItem, ReportTemplate,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail,
    StudentAppeal, PhotoAlbum, Photo, VideoContent, StudentLifeStatistic,
    EResourceCategory, EResource, EResourceFeature, InstructionFiles, Exchange
)





admin.site.register(Photo)
admin.site.register(InstructionFiles)
admin.site.register(Exchange)