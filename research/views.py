from rest_framework import generics, viewsets, status, filters
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q, Avg
from django.utils import timezone
from datetime import timedelta

from .models import (
    ScientificJournal, JournalIssue, JournalArticle
)
from .serializers import (
    ScientificJournalListSerializer, ScientificJournalDetailSerializer,
    JournalIssueListSerializer, JournalIssueDetailSerializer, JournalArticleSerializer
)



# ViewSet'ы для научных журналов
class ScientificJournalViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для научных журналов"""
    queryset = ScientificJournal.objects.filter(is_active=True).order_by('title_ru')
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title_ru', 'title_en', 'title_kg', 'description_ru', 'description_en', 'description_kg']
    ordering_fields = ['title_ru', 'established_year', 'impact_factor']
    ordering = ['title_ru']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ScientificJournalDetailSerializer
        return ScientificJournalListSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Основные журналы университета"""
        journals = self.get_queryset().filter(impact_factor__isnull=False).order_by('-impact_factor')[:3]
        serializer = ScientificJournalListSerializer(journals, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class JournalIssueViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для выпусков журналов"""
    queryset = JournalIssue.objects.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number')
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['journal', 'year', 'volume']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'description_ru', 'description_en', 'description_kg']
    ordering_fields = ['year', 'volume', 'number', 'publication_date']
    ordering = ['-year', '-volume', '-number']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return JournalIssueDetailSerializer
        return JournalIssueListSerializer

    @action(detail=False, methods=['get'])
    def by_journal(self, request):
        """Выпуски по журналам"""
        journal_id = request.GET.get('journal_id')
        if not journal_id:
            return Response({'error': 'journal_id parameter is required'}, status=400)
        
        issues = self.get_queryset().filter(journal_id=journal_id)
        
        # Группировка по годам
        years_data = {}
        for issue in issues:
            year = issue.year
            if year not in years_data:
                years_data[year] = []
            years_data[year].append(JournalIssueListSerializer(issue, context=self.get_serializer_context()).data)
        
        # Преобразуем в список для удобства фронтенда
        result = [{'year': year, 'issues': issues} for year, issues in sorted(years_data.items(), reverse=True)]
        return Response(result)

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Недавние выпуски"""
        issues = self.get_queryset()[:10]
        serializer = JournalIssueListSerializer(issues, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class JournalArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для статей журналов"""
    queryset = JournalArticle.objects.filter(is_active=True, issue__is_published=True).order_by('-issue__year', '-issue__volume', '-issue__number', 'order')
    serializer_class = JournalArticleSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['issue', 'issue__journal', 'is_open_access']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'authors_ru', 'authors_en', 'authors_kg', 'abstract_ru', 'abstract_en', 'abstract_kg']
    ordering_fields = ['published_date', 'citations_count', 'pages_start']
    ordering = ['-issue__year', '-issue__volume', '-issue__number', 'order']

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Недавние статьи"""
        articles = self.get_queryset()[:10]
        serializer = JournalArticleSerializer(articles, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def most_cited(self, request):
        """Наиболее цитируемые статьи"""
        articles = self.get_queryset().filter(citations_count__gt=0).order_by('-citations_count')[:10]
        serializer = JournalArticleSerializer(articles, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
