from django.urls import path
from .views import SubjectsDetailView, SubjectsListView

app_name = 'SubjectDetail'

urlpatterns = [
    path('', SubjectsListView.as_view(), name='subjects-list'),
    path('<int:pk>/', SubjectsDetailView.as_view(), name='subjects-detail'),
    # other URLs specific to MyModel or the app
]
