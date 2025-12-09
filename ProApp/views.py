from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, Question, Option
from .serializer import Course_serializer, Question_serializer, Option_serializer


class Course_view_set(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Course_serializer


class Question_view_set(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = Question_serializer


class Option_view_set(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = Option_serializer
