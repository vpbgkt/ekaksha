from django.urls import path
from .views import ClassNameListView, ClassNameDetailView

app_name = 'ClassName'

urlpatterns = [
    path('', ClassNameListView.as_view(), name='ClassName-list'),
    path('<int:pk>/', ClassNameDetailView.as_view(), name='ClassName-detail'),
    # other URLs specific to ClassName or the app
]
