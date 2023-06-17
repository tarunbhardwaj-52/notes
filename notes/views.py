from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class NoteListAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer

class NoteUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
