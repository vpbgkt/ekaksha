from django.shortcuts import render
from django.views.generic import ListView, DetailView
from SubjectDetail.models import Subjects

class SubjectListView(ListView):
    model = Subjects
    template_name = 'pages/subjects/subjects.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        # Get the class primary key from the URL parameters
        class_pk = self.kwargs['class_pk']

        # Filter subjects based on the class primary key
        queryset = Subjects.objects.filter(class_name_id=class_pk)

        return queryset

class SubjectsDetailView(DetailView):
    model = Subjects
    template_name = 'pages/subjects/subjectdetail.html'
    context_object_name = 'subjectdetails'


# from django.shortcuts import render
# from django.views import View
# from django.views.generic import ListView, DetailView
# from SubjectDetail.models import Subjects

# class SubjectsListView(ListView):
#     model = Subjects
#     template_name = 'index.html'
#     context_object_name = 'subjectdetails'
    
