from django.db import models


class ScientificJournal(models.Model):
    """Научные журналы университета"""
    title_ru = models.CharField("Название (рус)", max_length=300)
    title_en = models.CharField("Название (англ)", max_length=300)
    title_kg = models.CharField("Название (кыр)", max_length=300)
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    issn = models.CharField("ISSN", max_length=20, blank=True)
    eissn = models.CharField("E-ISSN", max_length=20, blank=True)
    
    editor_in_chief_ru = models.CharField("Главный редактор (рус)", max_length=200)
    editor_in_chief_en = models.CharField("Главный редактор (англ)", max_length=200)
    editor_in_chief_kg = models.CharField("Главный редактор (кыр)", max_length=200)
    
    editorial_board_ru = models.JSONField("Редакционная коллегия (рус)", default=list)
    editorial_board_en = models.JSONField("Редакционная коллегия (англ)", default=list)
    editorial_board_kg = models.JSONField("Редакционная коллегия (кыр)", default=list)
    
    publication_frequency_ru = models.CharField("Периодичность (рус)", max_length=100)
    publication_frequency_en = models.CharField("Периодичность (англ)", max_length=100)
    publication_frequency_kg = models.CharField("Периодичность (кыр)", max_length=100)
    
    scope_ru = models.TextField("Тематика (рус)", blank=True)
    scope_en = models.TextField("Тематика (англ)", blank=True)
    scope_kg = models.TextField("Тематика (кыр)", blank=True)
    
    submission_guidelines_ru = models.TextField("Требования к публикации (рус)", blank=True)
    submission_guidelines_en = models.TextField("Требования к публикации (англ)", blank=True)
    submission_guidelines_kg = models.TextField("Требования к публикации (кыр)", blank=True)
    
    cover_image = models.ImageField("Обложка", upload_to='research/journals/', blank=True)
    website = models.URLField("Веб-сайт", blank=True)
    contact_email = models.EmailField("Email", blank=True)
    
    established_year = models.IntegerField("Год основания")
    impact_factor = models.DecimalField("Импакт-фактор", max_digits=5, decimal_places=3, null=True, blank=True)
    
    is_open_access = models.BooleanField("Открытый доступ", default=True)
    is_peer_reviewed = models.BooleanField("Рецензируемый", default=True)
    is_active = models.BooleanField("Активно", default=True)
    
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Научный журнал"
        verbose_name_plural = "Научные журналы"
        ordering = ['title_ru']
        
    def __str__(self):
        return self.title_ru


class JournalIssue(models.Model):
    """Выпуски журналов"""
    journal = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, related_name='issues', verbose_name="Журнал")
    
    volume = models.PositiveIntegerField("Том")
    number = models.PositiveIntegerField("Номер")
    year = models.PositiveIntegerField("Год")
    
    title_ru = models.CharField("Название выпуска (рус)", max_length=300, blank=True)
    title_en = models.CharField("Название выпуска (англ)", max_length=300, blank=True)
    title_kg = models.CharField("Название выпуска (кыр)", max_length=300, blank=True)
    
    publication_date = models.DateField("Дата публикации")
    
    description_ru = models.TextField("Описание (рус)", blank=True)
    description_en = models.TextField("Описание (англ)", blank=True)
    description_kg = models.TextField("Описание (кыр)", blank=True)
    
    cover_image = models.ImageField("Обложка выпуска", upload_to='research/journal_issues/', blank=True)
    pdf_file = models.FileField("PDF файл", upload_to='research/journal_issues/pdf/', blank=True)
    
    doi = models.CharField("DOI выпуска", max_length=100, blank=True)
    pages_count = models.PositiveIntegerField("Количество страниц", null=True, blank=True)
    articles_count = models.PositiveIntegerField("Количество статей", default=0)
    
    is_published = models.BooleanField("Опубликован", default=False)
    is_active = models.BooleanField("Активно", default=True)
    
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    
    class Meta:
        verbose_name = "Выпуск журнала"
        verbose_name_plural = "Выпуски журналов"
        ordering = ['-year', '-volume', '-number']
        unique_together = ['journal', 'volume', 'number', 'year']
        
    def __str__(self):
        return f"{self.journal.title_ru} - Том {self.volume}, №{self.number} ({self.year})"


class JournalArticle(models.Model):
    """Статьи в журналах"""
    issue = models.ForeignKey(JournalIssue, on_delete=models.CASCADE, related_name='articles', verbose_name="Выпуск")
    
    title_ru = models.CharField("Название (рус)", max_length=500)
    title_en = models.CharField("Название (англ)", max_length=500)
    title_kg = models.CharField("Название (кыр)", max_length=500)
    
    authors_ru = models.CharField("Авторы (рус)", max_length=500)
    authors_en = models.CharField("Авторы (англ)", max_length=500)
    authors_kg = models.CharField("Авторы (кыр)", max_length=500)
    
    abstract_ru = models.TextField("Аннотация (рус)")
    abstract_en = models.TextField("Аннотация (англ)")
    abstract_kg = models.TextField("Аннотация (кыр)")
    
    keywords_ru = models.JSONField("Ключевые слова (рус)", default=list)
    keywords_en = models.JSONField("Ключевые слова (англ)", default=list)
    keywords_kg = models.JSONField("Ключевые слова (кыр)", default=list)
    
    pages_start = models.PositiveIntegerField("Страница начала")
    pages_end = models.PositiveIntegerField("Страница окончания")
    
    doi = models.CharField("DOI статьи", max_length=100, blank=True)
    pdf_file = models.FileField("PDF файл статьи", upload_to='research/journal_articles/', blank=True)
    
    received_date = models.DateField("Дата поступления", null=True, blank=True)
    accepted_date = models.DateField("Дата принятия", null=True, blank=True)
    published_date = models.DateField("Дата публикации", null=True, blank=True)
    
    citations_count = models.PositiveIntegerField("Количество цитирований", default=0)
    
    order = models.PositiveIntegerField("Порядок в выпуске", default=0)
    
    is_open_access = models.BooleanField("Открытый доступ", default=True)
    is_active = models.BooleanField("Активно", default=True)
    
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Статья журнала"
        verbose_name_plural = "Статьи журналов"
        ordering = ['issue', 'order', 'pages_start']
        
    def __str__(self):
        return f"{self.title_ru} ({self.issue})"