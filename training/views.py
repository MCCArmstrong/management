from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Courses


class CourseHome(ListView):
    template_name = 'it-training/courseHome.html'
    queryset = Courses.objects.all().order_by("id")[:1]

