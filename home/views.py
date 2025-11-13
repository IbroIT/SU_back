from django.shortcuts import render
from .models import Numbers, Testimonials
from .serializers import NumbersSerializer, TestimonialsSerializer
from rest_framework import generics

from .models import linksNavbar
from .serializers import LinksNavbarSerializer

class LinksNavbarListView(generics.ListAPIView):
    queryset = linksNavbar.objects.all()
    serializer_class = LinksNavbarSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
# Create your views here.
class NumberListView(generics.ListAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
class TestimonialListView(generics.ListAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context