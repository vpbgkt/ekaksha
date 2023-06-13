# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data = {
        'title': 'home new'
    }
    return render(request, 'index.html', data)

def contect(request):
    return render(request, 'pages/basic/contect.html')

def aboutus(request):
    return render(request, 'pages/basic/aboutus.html', {'navbar': 'aboutus'})

