from rest_framework import serializers
from .models import Course, Question, Option


class Option_serializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class Question_serializer(serializers.ModelSerializer):
    options = Option_serializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class Course_serializer(serializers.ModelSerializer):
    questions = Question_serializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
