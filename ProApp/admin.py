from django.contrib import admin

# Register your models here.

from .models import Course, Question, Option

# Inline Options inside Question


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # shows 4 empty option fields by default

# Inline Questions inside Course


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # shows 1 empty question field by default


# Admin for Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # columns shown in course list
    list_display = ("title", "code", "description", "outline")
    search_fields = ("title", "code")  # adds a search box
    inlines = [QuestionInline]  # add questions inline


# Admin for Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # columns shown in question list
    list_display = ("question_text", "course")
    search_fields = ("question_text",)  # search box
    inlines = [OptionInline]  # add options inline


# Admin for Option
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    # columns shown in option list
    list_display = ("option_text", "is_correct", "question")
    list_filter = ("is_correct",)  # filter correct/incorrect options
    search_fields = ("option_text",)
