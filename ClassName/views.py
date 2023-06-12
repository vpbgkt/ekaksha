from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from ClassName.models import ClassName

class ClassNameListView(ListView):
    model = ClassName
    template_name = 'pages/classeslist.html'
    context_object_name = 'ClassListData'
    
class ClassNameDetailView(DetailView):
    model = ClassName
    template_name = 'pages/classesdetails.html'
    context_object_name = 'ClassDetaildata'
    
