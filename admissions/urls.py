from django.urls import path, include

from banner import views
from .views import BankRequisitesViewSet, submit_application_email
from rest_framework.routers import DefaultRouter
from .views import RequirementViewSet
from . import views

router = DefaultRouter()
router.register(r'requirements', RequirementViewSet, basename='requirement')
router.register(r'bank-requisites-kg', BankRequisitesViewSet, basename='bank-requisites-kg')

urlpatterns = [

    path('applications/submit-email/', submit_application_email, name='submit_application_email'),
    path('', include(router.urls)),
    path('faqs/', views.FAQListView.as_view(), name='faq-list'),
    path('fees/', views.FeeListView.as_view(), name='fee-list'),
    path('contacts/', views.ContactsListView.as_view(), name='contacts-list'),
    path('fees-foreign/', views.FeeForeignListView.as_view(), name='fee-foreign-list'),
    path('requisities-foreign/', views.RequisitiesForeignListView.as_view(), name='requisities-foreign-list'),
    path('contacts-foreign/', views.ContactForeignListView.as_view(), name='contacts-foreign-list'),
]
