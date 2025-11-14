from django.urls import path
from . import views

urlpatterns = [
    # Partner endpoints
    path('partners/', views.PartnerListView.as_view(), name='partner-list'),
    path('partners/<int:id>/', views.PartnerDetailView.as_view(), name='partner-detail'),
    path('partners/frontend/', views.partners_for_frontend, name='partners-frontend'),
    path('partners/stats/', views.partners_stats, name='partners-stats'),
]