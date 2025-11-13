from .models import Testimonials, Numbers
from rest_framework import serializers

from .models import linksNavbar


# Сериализатор для linksNavbar с поддержкой всех языков
class LinksNavbarSerializer(serializers.ModelSerializer):
    name_ru = serializers.CharField(read_only=True)
    name_kg = serializers.CharField(read_only=True)
    name_en = serializers.CharField(read_only=True)

    class Meta:
        model = linksNavbar
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'url']

class NumbersSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    description_ru = serializers.CharField(read_only=True)
    description_en = serializers.CharField(read_only=True)
    description_kg = serializers.CharField(read_only=True)

    class Meta:
        model = Numbers
        fields = ['id', 'icon', 'number', 'description', 'description_ru', 'description_en', 'description_kg']
    
    def get_description(self, obj):
        request = self.context.get('request')
        lang = 'en'
        if request:
            lang = getattr(request, 'LANGUAGE_CODE', None) or request.query_params.get('lang', 'en')
        return obj.get_description(lang)
    
class TestimonialsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    testimonial = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    name_ru = serializers.CharField(read_only=True)
    name_en = serializers.CharField(read_only=True)
    name_kg = serializers.CharField(read_only=True)
    testimonial_ru = serializers.CharField(read_only=True)
    testimonial_en = serializers.CharField(read_only=True)
    testimonial_kg = serializers.CharField(read_only=True)
    faculty_ru = serializers.CharField(read_only=True)
    faculty_en = serializers.CharField(read_only=True)
    faculty_kg = serializers.CharField(read_only=True)

    class Meta:
        model = Testimonials
        fields = [
            'id', 'photo', 'year',
            'name', 'testimonial', 'faculty',
            'name_ru', 'name_en', 'name_kg',
            'testimonial_ru', 'testimonial_en', 'testimonial_kg',
            'faculty_ru', 'faculty_en', 'faculty_kg',
        ]
    
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
    

    
