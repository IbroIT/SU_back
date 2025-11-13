from django.db import models

class requirement(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, verbose_name='Title in English')
    title_kg = models.CharField(max_length=200, verbose_name='Title in Kyrgyz')
    description_ru = models.TextField(verbose_name='Description in Russian')
    description_en = models.TextField(verbose_name='Description in English')
    description_kg = models.TextField(verbose_name='Description in Kyrgyz')

    def __str__(self):
        return self.title_ru
    
    def get_title(self, lang='ru'):
        return getattr(self, f'title_{lang}', self.title_ru)
    
    def get_description(self, lang='ru'):
        return getattr(self, f'description_{lang}', self.description_ru)
    


class BankRequisites(models.Model):
    bank_name_ru = models.CharField(max_length=200)
    bank_name_en = models.CharField(max_length=200, verbose_name='Bank name in English')
    bank_name_kg = models.CharField(max_length=200, verbose_name='Bank name in Kyrgyz')
    account_number = models.CharField(max_length=50)
    bik = models.CharField(max_length=20)
    inn = models.CharField(max_length=20)
    recipient_ru = models.CharField(max_length=300)
    recipient_en = models.CharField(max_length=300, verbose_name='Recipient in English')
    recipient_kg = models.CharField(max_length=300, verbose_name='Recipient in Kyrgyz')
    payment_purpose_ru = models.CharField(max_length=500)
    payment_purpose_en = models.CharField(max_length=500, verbose_name='Payment purpose in English')
    payment_purpose_kg = models.CharField(max_length=500, verbose_name='Payment purpose in Kyrgyz')

    def __str__(self):
        return self.bank_name_ru

    def get_bank_name(self, lang='ru'):
        return getattr(self, f'bank_name_{lang}', self.bank_name_ru)

    def get_recipient(self, lang='ru'):
        return getattr(self, f'recipient_{lang}', self.recipient_ru)

    def get_payment_purpose(self, lang='ru'):
        return getattr(self, f'payment_purpose_{lang}', self.payment_purpose_ru)
    
class Fee(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, verbose_name='Title in English')
    title_kg = models.CharField(max_length=200, verbose_name='Title in Kyrgyz')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='В сомах')
    faculty_ru = models.CharField(max_length=200, verbose_name='Faculty in Russian')
    faculty_en = models.CharField(max_length=200, verbose_name='Faculty in English')
    faculty_kg = models.CharField(max_length=200, verbose_name='Faculty in Kyrgyz')

    warnings_ru = models.JSONField(blank=True, null=True, verbose_name='Warnings')
    warnings_en = models.JSONField(blank=True, null=True, verbose_name='Warnings')
    warnings_kg = models.JSONField(blank=True, null=True, verbose_name='Warnings')

    class Meta:
        verbose_name = 'цена контракта(kg)'
        verbose_name_plural = 'цены контрактов(kg)'

    def __str__(self):
        return self.title_ru
    def get_title(self, lang='ru'):
        return getattr(self, f'title_{lang}', self.title_ru)
    def get_faculty(self, lang='ru'):
        return getattr(self, f'faculty_{lang}', self.faculty_ru)
    def get_warnings(self, lang='ru'):
        return getattr(self, f'warnings_{lang}', self.warnings_ru)

class Contacts(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    def __str__(self):
        return self.phone_number
    
class FeeForeign(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, verbose_name='Title in English')
    title_kg = models.CharField(max_length=200, verbose_name='Title in Kyrgyz')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='В долларах')
    faculty_ru = models.CharField(max_length=200, verbose_name='Faculty in Russian')
    faculty_en = models.CharField(max_length=200, verbose_name='Faculty in English')
    faculty_kg = models.CharField(max_length=200, verbose_name='Faculty in Kyrgyz')

    warnings_ru = models.JSONField(blank=True, null=True, verbose_name='Warnings')
    warnings_en = models.JSONField(blank=True, null=True, verbose_name='Warnings')
    warnings_kg = models.JSONField(blank=True, null=True, verbose_name='Warnings')


    class Meta:
        verbose_name = 'цена контракта(иностранный)'
        verbose_name_plural = 'цены контрактов(иностранный)'
    
    def __str__(self):
        return self.title_ru
    def get_title(self, lang='ru'):
        return getattr(self, f'title_{lang}', self.title_ru)
    def get_faculty(self, lang='ru'):
        return getattr(self, f'faculty_{lang}', self.faculty_ru)
    def get_warnings(self, lang='ru'):
        return getattr(self, f'warnings_{lang}', self.warnings_ru)
    
class RequisitiesForeign(models.Model):
    bank_name_ru = models.CharField(max_length=200)
    bank_name_en = models.CharField(max_length=200, verbose_name='Bank name in English')
    bank_name_kg = models.CharField(max_length=200, verbose_name='Bank name in Kyrgyz')
    account_number = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=20)
    recipient_ru = models.CharField(max_length=300)
    recipient_en = models.CharField(max_length=300, verbose_name='Recipient in English')
    recipient_kg = models.CharField(max_length=300, verbose_name='Recipient in Kyrgyz')
    correspondent_bank = models.CharField(max_length=300, verbose_name='Correspondent Bank')
    warnings_ru = models.JSONField(blank=True, null=True, verbose_name='Warnings')
    warnings_en = models.JSONField(blank=True, null=True, verbose_name='Warnings')  
    warnings_kg = models.JSONField(blank=True, null=True, verbose_name='Warnings')

    class Meta:
        verbose_name = 'Requisities for foreign students'
        verbose_name_plural = 'Requisities for foreign students'

    def __str__(self):
        return self.bank_name_ru

    def get_bank_name(self, lang='ru'):
        return getattr(self, f'bank_name_{lang}', self.bank_name_ru)

    def get_recipient(self, lang='ru'):
        return getattr(self, f'recipient_{lang}', self.recipient_ru)
    def get_warnings(self, lang='ru'):
        return getattr(self, f'warnings_{lang}', self.warnings_ru)


class ContactForeign(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    telegram = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Contact for foreign students'
        verbose_name_plural = 'Contacts for foreign students'
    def __str__(self):
        return self.phone_number
    
class FAQ(models.Model):
    question_ru = models.CharField(max_length=300)
    question_en = models.CharField(max_length=300, verbose_name='Question in English')
    question_kg = models.CharField(max_length=300, verbose_name='Question in Kyrgyz')
    answer_ru = models.TextField(verbose_name='Answer in Russian')
    answer_en = models.TextField(verbose_name='Answer in English')
    answer_kg = models.TextField(verbose_name='Answer in Kyrgyz')

    def __str__(self):
        return self.question_ru
    
    def get_question(self, lang='ru'):
        return getattr(self, f'question_{lang}', self.question_ru)
    
    def get_answer(self, lang='ru'):
        return getattr(self, f'answer_{lang}', self.answer_ru) 
    

