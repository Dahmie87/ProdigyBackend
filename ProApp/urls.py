from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Course_view_set, Question_view_set, Option_view_set

api_router = DefaultRouter()
api_router.register(r'courses', Course_view_set, basename="course")
api_router.register(r'questions', Question_view_set, basename="question")
api_router.register(r'options', Option_view_set, basename="option")

urlpatterns = [
    path('', include(api_router.urls)),

]
