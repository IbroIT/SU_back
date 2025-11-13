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
    
