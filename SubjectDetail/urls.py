from django.urls import path
from .views import SubjectListView

app_name = 'SubjectDetail'

urlpatterns = [
    # path('subject/<int:pk>/', SubjectsDetailView.as_view(), name='subject-detail'),
    # path('subject/<int:class_pk>/', SubjectListView.as_view(), name='subject_list'),
    path('course/<int:class_pk>/subjects/', SubjectListView.as_view(), name='subject_list'),

    
    # other URLs specific to SubjectDetail
]