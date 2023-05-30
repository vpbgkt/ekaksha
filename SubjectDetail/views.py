from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from SubjectDetail.models import Subjects

class SubjectsListView(ListView):
    model = Subjects
    template_name = 'index.html'
    context_object_name = 'subjectdetails'
    
class SubjectsDetailView(DetailView):
    model = Subjects
    template_name = 'index.html'
    context_object_name = 'subjectdetails'