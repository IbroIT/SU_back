from rest_framework import serializers
from .models import ScientificJournal, JournalIssue, JournalArticle


# Сериализаторы для научных журналов
class JournalArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для статей журнала"""
    
    class Meta:
        model = JournalArticle
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'authors_ru', 'authors_en', 'authors_kg',
            'abstract_ru', 'abstract_en', 'abstract_kg',
            'keywords_ru', 'keywords_en', 'keywords_kg',
            'pages_start', 'pages_end', 'doi', 'pdf_file',
            'received_date', 'accepted_date', 'published_date',
            'citations_count', 'order', 'is_open_access'
        ]


class JournalIssueListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка выпусков журнала"""
    journal_title = serializers.CharField(source='journal.title_ru', read_only=True)
    
    class Meta:
        model = JournalIssue
        fields = [
            'id', 'volume', 'number', 'year', 'publication_date',
            'title_ru', 'title_en', 'title_kg',
            'cover_image', 'pdf_file', 'doi',
            'pages_count', 'articles_count', 'is_published',
            'journal_title'
        ]


class JournalIssueDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о выпуске журнала"""
    journal = serializers.StringRelatedField(read_only=True)
    articles = JournalArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = JournalIssue
        fields = [
            'id', 'journal', 'volume', 'number', 'year', 'publication_date',
            'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'cover_image', 'pdf_file', 'doi',
            'pages_count', 'articles_count', 'is_published',
            'articles', 'created_at'
        ]


class ScientificJournalListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка научных журналов"""
    latest_issue = serializers.SerializerMethodField()
    issues_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ScientificJournal
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'issn', 'eissn', 'editor_in_chief_ru', 'editor_in_chief_en', 'editor_in_chief_kg',
            'publication_frequency_ru', 'publication_frequency_en', 'publication_frequency_kg',
            'cover_image', 'website', 'established_year', 'impact_factor',
            'is_open_access', 'is_peer_reviewed',
            'latest_issue', 'issues_count'
        ]
    
    def get_latest_issue(self, obj):
        latest = obj.issues.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number').first()
        if latest:
            return JournalIssueListSerializer(latest).data
        return None
    
    def get_issues_count(self, obj):
        return obj.issues.filter(is_published=True, is_active=True).count()


class ScientificJournalDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о научном журнале"""
    recent_issues = serializers.SerializerMethodField()
    issues_by_year = serializers.SerializerMethodField()
    
    class Meta:
        model = ScientificJournal
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'issn', 'eissn', 'editor_in_chief_ru', 'editor_in_chief_en', 'editor_in_chief_kg',
            'editorial_board_ru', 'editorial_board_en', 'editorial_board_kg',
            'publication_frequency_ru', 'publication_frequency_en', 'publication_frequency_kg',
            'scope_ru', 'scope_en', 'scope_kg',
            'submission_guidelines_ru', 'submission_guidelines_en', 'submission_guidelines_kg',
            'cover_image', 'website', 'contact_email', 'established_year', 'impact_factor',
            'is_open_access', 'is_peer_reviewed',
            'recent_issues', 'issues_by_year', 'created_at'
        ]
    
    def get_recent_issues(self, obj):
        recent = obj.issues.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number')[:5]
        return JournalIssueListSerializer(recent, many=True).data
    
    def get_issues_by_year(self, obj):
        """Группировка выпусков по годам для архива"""
        issues = obj.issues.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number')
        
        years_data = {}
        for issue in issues:
            year = issue.year
            if year not in years_data:
                years_data[year] = []
            years_data[year].append(JournalIssueListSerializer(issue).data)
        
        # Преобразуем в список для удобства фронтенда
        return [{'year': year, 'issues': issues} for year, issues in sorted(years_data.items(), reverse=True)]