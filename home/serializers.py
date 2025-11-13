from .models import Testimonials, Numbers
from rest_framework import serializers

from .models import linksNavbar

class LinksNavbarSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = linksNavbar
        fields = ['id', 'name', 'url']

    def get_name(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'ru') if request else 'ru'
        return obj.get_name(lang)

class NumbersSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Numbers
        fields = ['id', 'icon', 'number', 'description']
    
    def get_description(self, obj):
        request = self.context.get('request')
        lang = request.LANGUAGE_CODE if request else 'en'
        return obj.get_description(lang)
    
class TestimonialsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    testimonial = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()

    class Meta:
        model = Testimonials
        fields = ['id', 'photo', 'year', 'name', 'testimonial', 'faculty']
    
    def get_name(self, obj):
        request = self.context.get('request')
        lang = request.LANGUAGE_CODE if request else 'en'
        return obj.get_name(lang)
    
    def get_testimonial(self, obj):
        request = self.context.get('request')
        lang = request.LANGUAGE_CODE if request else 'en'
        return obj.get_testimonial(lang)
    
    def get_faculty(self, obj):
        request = self.context.get('request')
        lang = request.LANGUAGE_CODE if request else 'en'
        return obj.get_faculty(lang)
    

    
