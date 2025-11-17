from rest_framework import serializers
from .models import ScheduleSubsection

class ScheduleSubsectionSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = ScheduleSubsection
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg', 'pdf_url', 'is_active', 'order'
        ]

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        if obj.pdf_file:
            if request:
                return request.build_absolute_uri(obj.pdf_file.url)
            return obj.pdf_file.url
        return None
