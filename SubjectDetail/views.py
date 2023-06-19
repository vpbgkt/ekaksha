from django.shortcuts import render
from django.views.generic import ListView, DetailView
from SubjectDetail.models import Subjects
from ClassName.models import ClassName

class SubjectListView(ListView):
    model = Subjects
    template_name = 'pages/subjects/subjects.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        # Get the class primary key from the URL parameters
        class_pk = self.kwargs['class_pk']

        # Filter subjects based on the class primary key
        queryset = Subjects.objects.filter(class_name__pk=class_pk)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the class details based on the primary key
        class_pk = self.kwargs['class_pk']
        class_instance = ClassName.objects.get(pk=class_pk)

        # Add the class details to the context
        context['class_name'] = class_instance.title
        context['class_description'] = class_instance.description
        # Add other class fields as needed

        return context

class SubjectsDetailView(DetailView):
    model = Subjects
    template_name = 'pages/subjects/subjectdetail.html'
    context_object_name = 'subjectdetails'