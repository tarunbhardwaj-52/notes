from django.urls import path
from .views import *

urlpatterns = [
    path('', NoteListAPIView.as_view(), name='note-list-create'),
    path('<int:pk>/', NoteUpdateDeleteAPIView.as_view(), name='note-retrieve-update-delete'),
]
