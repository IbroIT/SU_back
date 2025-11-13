from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NumberListView, TestimonialListView
from . import views

urlpatterns = [
    path('numbers/', NumberListView.as_view(), name='number-list'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('navbar-links/', views.LinksNavbarListView.as_view(), name='navbar-links-list'),
]