from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.CharField()
    outline = models.CharField()


class Question(models.Model):
    # question field in course
    course = models.ForeignKey(
        Course, related_name="questions", on_delete=models.CASCADE)

    question_text = models.CharField(max_length=10000)


class Option(models.Model):
    question = models.ForeignKey(
        Question, related_name="options", on_delete=models.CASCADE)

    option_text = models.CharField(max_length=10000)
    is_correct = models.BooleanField()
