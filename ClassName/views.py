from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from ClassName.models import ClassName

class ClassNameListView(ListView):
    model = ClassName
    template_name = 'index.html'
    context_object_name = 'classname'
    
class ClassNameDetailView(DetailView):
    model = ClassName
    template_name = 'index.html'
    context_object_name = 'classname'

# def eclass_list(request):
#     eclasses = Eclass.objects.all()
#     context = {'eclasses': eclasses}
#     return render(request, 'pages/classeslist.html', context)

