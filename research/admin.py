from django.contrib import admin
from .models import ScientificJournal, JournalIssue, JournalArticle


# Админ для научных журналов
@admin.register(ScientificJournal)
class ScientificJournalAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'established_year', 'impact_factor', 'is_open_access', 'is_peer_reviewed', 'is_active']
    list_filter = ['is_open_access', 'is_peer_reviewed', 'is_active', 'established_year']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'issn', 'eissn']
    list_editable = ['impact_factor', 'is_open_access', 'is_peer_reviewed', 'is_active']
    ordering = ['title_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'established_year')
        }),
        ('Идентификаторы', {
            'fields': ('issn', 'eissn')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Редакция', {
            'fields': ('editor_in_chief_ru', 'editor_in_chief_en', 'editor_in_chief_kg')
        }),
        ('Редакционная коллегия', {
            'fields': ('editorial_board_ru', 'editorial_board_en', 'editorial_board_kg')
        }),
        ('Публикация', {
            'fields': ('publication_frequency_ru', 'publication_frequency_en', 'publication_frequency_kg')
        }),
        ('Тематика', {
            'fields': ('scope_ru', 'scope_en', 'scope_kg')
        }),
        ('Требования к публикации', {
            'fields': ('submission_guidelines_ru', 'submission_guidelines_en', 'submission_guidelines_kg')
        }),
        ('Медиа', {
            'fields': ('cover_image',)
        }),
        ('Контакты', {
            'fields': ('website', 'contact_email')
        }),
        ('Метрики', {
            'fields': ('impact_factor',)
        }),
        ('Настройки', {
            'fields': ('is_open_access', 'is_peer_reviewed', 'is_active')
        }),
    )


class JournalArticleInline(admin.TabularInline):
    model = JournalArticle
    extra = 0
    fields = ['title_ru', 'authors_ru', 'pages_start', 'pages_end', 'order', 'is_active']
    readonly_fields = ['created_at']


@admin.register(JournalIssue)
class JournalIssueAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'publication_date', 'articles_count', 'pages_count', 'is_published', 'is_active']
    list_filter = ['journal', 'year', 'is_published', 'is_active', 'publication_date']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'description_ru', 'description_en', 'description_kg']
    list_editable = ['is_published', 'is_active']
    ordering = ['-year', '-volume', '-number']
    raw_id_fields = ['journal']
    inlines = [JournalArticleInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('journal', 'volume', 'number', 'year', 'publication_date')
        }),
        ('Название', {
            'fields': ('title_ru', 'title_en', 'title_kg')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Медиа', {
            'fields': ('cover_image', 'pdf_file')
        }),
        ('Метаданные', {
            'fields': ('doi', 'pages_count', 'articles_count')
        }),
        ('Настройки', {
            'fields': ('is_published', 'is_active')
        }),
    )


@admin.register(JournalArticle)
class JournalArticleAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'issue', 'authors_ru', 'pages_start', 'pages_end', 'citations_count', 'is_active']
    list_filter = ['issue__journal', 'issue__year', 'is_open_access', 'is_active', 'published_date']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'authors_ru', 'authors_en', 'authors_kg', 'abstract_ru', 'abstract_en', 'abstract_kg']
    list_editable = ['citations_count', 'is_active']
    ordering = ['-issue__year', '-issue__volume', '-issue__number', 'order']
    raw_id_fields = ['issue']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('issue', 'title_ru', 'title_en', 'title_kg', 'order')
        }),
        ('Авторы', {
            'fields': ('authors_ru', 'authors_en', 'authors_kg')
        }),
        ('Аннотация', {
            'fields': ('abstract_ru', 'abstract_en', 'abstract_kg')
        }),
        ('Ключевые слова', {
            'fields': ('keywords_ru', 'keywords_en', 'keywords_kg')
        }),
        ('Страницы', {
            'fields': ('pages_start', 'pages_end')
        }),
        ('Идентификаторы', {
            'fields': ('doi',)
        }),
        ('Файлы', {
            'fields': ('pdf_file',)
        }),
        ('Даты', {
            'fields': ('received_date', 'accepted_date', 'published_date')
        }),
        ('Метрики', {
            'fields': ('citations_count',)
        }),
        ('Настройки', {
            'fields': ('is_open_access', 'is_active')
        }),
    )
