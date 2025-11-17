from django.db import models

class ScheduleSubsection(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name="Название (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Название (EN)", blank=True)
    title_kg = models.CharField(max_length=200, verbose_name="Название (KG)", blank=True)
    pdf_file = models.FileField(upload_to='schedule/pdfs/', verbose_name="PDF файл")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Подраздел расписания"
        verbose_name_plural = "Подразделы расписания"
        ordering = ['order', 'title_ru']

    def __str__(self):
        return self.title_ru
