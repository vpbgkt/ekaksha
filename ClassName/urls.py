from django.urls import path
from .views import ClassNameDetailView, ClassNameListView

app_name = 'ClassName'

urlpatterns = [
    path('', ClassNameListView.as_view(), name='ClassName-list'),
    path('<str:title>/', ClassNameDetailView.as_view(), name='ClassName-detail'),
    # other URLs specific to ClassName or the app

]
