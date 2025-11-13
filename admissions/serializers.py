# serializers.py
from rest_framework import serializers
from .models import BankRequisites, requirement, Fee, Contacts, FeeForeign, RequisitiesForeign, ContactForeign


class RequirementSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_title(lang)

    def get_description(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_description(lang)

    class Meta:
        model = requirement
        fields = ['id', 'title', 'description']

class BankRequisitesSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField()
    recipient = serializers.SerializerMethodField()
    payment_purpose = serializers.SerializerMethodField()

    def get_bank_name(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_bank_name(lang)

    def get_recipient(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_recipient(lang)

    def get_payment_purpose(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_payment_purpose(lang)

    class Meta:
        model = BankRequisites  
        fields = ['id', 'bank_name', 'account_number', 'bik', 'inn', 'recipient', 'payment_purpose']


class FeeSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    warnings = serializers.SerializerMethodField()

    class Meta:
        model = Fee
        fields = ['id', 'title', 'amount', 'faculty', 'warnings']

    def get_title(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_title(lang)

    def get_faculty(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_faculty(lang)

    def get_warnings(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_warnings(lang)

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'phone_number', 'email', 'working_hours']

class FeeForeignSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    warnings = serializers.SerializerMethodField()

    class Meta:
        model = FeeForeign
        fields = ['id', 'title', 'amount', 'faculty', 'warnings']

    def get_title(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_title(lang)

    def get_faculty(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_faculty(lang)

    def get_warnings(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_warnings(lang)

class RequisitiesForeignSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField()
    recipient = serializers.SerializerMethodField()
    warnings = serializers.SerializerMethodField()

    class Meta:
        model = RequisitiesForeign
        fields = ['id', 'bank_name', 'account_number', 'swift_code', 'recipient', 'correspondent_bank', 'warnings']

    def get_bank_name(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_bank_name(lang)

    def get_recipient(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_recipient(lang)

    def get_warnings(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_warnings(lang)

class ContactForeignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForeign
        fields = ['id', 'phone_number', 'email', 'whatsapp', 'telegram']

from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_question(lang)

    def get_answer(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_answer(lang)
    

