from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Создаем роутер для ViewSets
router = DefaultRouter()

# ViewSets для научных журналов
router.register(r'journals', views.ScientificJournalViewSet, basename='scientificjournal')
router.register(r'journal-issues', views.JournalIssueViewSet, basename='journalissue')
router.register(r'journal-articles', views.JournalArticleViewSet, basename='journalarticle')

app_name = 'research'

urlpatterns = [
    # API endpoints через router
    path('api/', include(router.urls)),
]

"""
Доступные API endpoints:

НАУЧНЫЕ ЖУРНАЛЫ:
GET /research/api/journals/ - список научных журналов
GET /research/api/journals/{id}/ - детали журнала
GET /research/api/journals/featured/ - основные журналы университета

ВЫПУСКИ ЖУРНАЛОВ:
GET /research/api/journal-issues/ - список выпусков журналов
GET /research/api/journal-issues/{id}/ - детали выпуска
GET /research/api/journal-issues/by_journal/?journal_id={id} - выпуски по журналам
GET /research/api/journal-issues/recent/ - недавние выпуски

СТАТЬИ ЖУРНАЛОВ:
GET /research/api/journal-articles/ - список статей
GET /research/api/journal-articles/{id}/ - детали статьи
GET /research/api/journal-articles/recent/ - недавние статьи
GET /research/api/journal-articles/most_cited/ - наиболее цитируемые статьи

Параметры фильтрации для выпусков:
- journal: ID журнала
- year: год выпуска
- volume: том
- search: поиск по названию, описанию

Параметры фильтрации для статей:
- issue: ID выпуска
- issue__journal: ID журнала
- is_open_access: true/false
- search: поиск по названию, авторам, аннотации
"""
