from django.db import models


class Numbers(models.Model):
    icon = models.ImageField(upload_to='numbers/icons')
    number = models.CharField(max_length=20)
    description_ru = models.CharField(max_length=255, verbose_name='Описание (RU)')
    description_kg = models.CharField(max_length=255, verbose_name='Описание (kg)')
    description_en = models.CharField(max_length=255, verbose_name='Описание (en)')

    class Meta:
        verbose_name = 'секция цифры'
        verbose_name_plural = 'секция цифры'
    
    def __str__(self):
        return self.number + " - " + self.description_en
    
    def get_description(self, lang):
        return getattr(self, f'description_{lang}', self.description_en)
    
class Testimonials(models.Model):
    photo = models.ImageField(upload_to='testimonials/photos')
    year = models.CharField(max_length=10, verbose_name='в каком курсе учится студент')
    name_ru = models.CharField(max_length=100, verbose_name='Имя студента (RU)')
    name_kg = models.CharField(max_length=100, verbose_name='Имя студента (kg)')
    name_en = models.CharField(max_length=100, verbose_name='Имя студента (en)')
    testimonial_ru = models.TextField(verbose_name='Отзыв студента (RU)')
    testimonial_kg = models.TextField(verbose_name='Отзыв студента (kg)')
    testimonial_en = models.TextField(verbose_name='Отзыв студента (en)')
    faculty_ru = models.CharField(max_length=100, verbose_name='Факультет студента (RU)')
    faculty_kg = models.CharField(max_length=100, verbose_name='Факультет студента (kg)')
    faculty_en = models.CharField(max_length=100, verbose_name='Факультет студента (en)')
    
    class Meta:
        verbose_name = 'отзыв студента'
        verbose_name_plural = 'отзывы студентов'
    
    def __str__(self):
        return self.name_en + " - " + self.year
    def get_name(self, lang):
        return getattr(self, f'name_{lang}', self.name_en)
    def get_testimonial(self, lang):
        return getattr(self, f'testimonial_{lang}', self.testimonial_en)
    def get_faculty(self, lang):
        return getattr(self, f'faculty_{lang}', self.faculty_en)
    

class linksNavbar(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='Имя ссылки (RU)')
    name_kg = models.CharField(max_length=100, verbose_name='Имя ссылки (kg)')
    name_en = models.CharField(max_length=100, verbose_name='Имя ссылки (en)')
    url = models.URLField(verbose_name='URL ссылки')

    class Meta:
        verbose_name = 'ссылка навигационной панели'
        verbose_name_plural = 'ссылки навигационной панели'
    
    def __str__(self):
        return self.name_en
    
    def get_name(self, lang):
        return getattr(self, f'name_{lang}', self.name_en)