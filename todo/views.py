from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import TodoSerializer

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TodoSerializer