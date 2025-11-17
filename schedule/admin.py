from django.contrib import admin
from .models import ScheduleSubsection

@admin.register(ScheduleSubsection)
class ScheduleSubsectionAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_en', 'title_kg', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('title_ru', 'title_en', 'title_kg')
    ordering = ('order', 'title_ru')
    fieldsets = (
        (None, {
            'fields': ('title_ru', 'title_en', 'title_kg', 'pdf_file', 'is_active', 'order')
        }),
    )
