from django.urls import path
from . import views

# app_name = 'training'

urlpatterns = [
    path('courses/', views.CourseHome.as_view(), name='course-home')
]