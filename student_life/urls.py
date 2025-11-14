from django.urls import path
from . import views

urlpatterns = [
    path('instruction-files/', views.InstructionFilesListView.as_view(), name='instruction-files-list'),
    path('api/photos/', views.PhotoListView.as_view(), name='photo_list'),
]
