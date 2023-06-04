from django.urls import path
from .views import SubjectListView

app_name = 'SubjectDetail'

urlpatterns = [
    path('course/<int:class_pk>/', SubjectListView.as_view(), name='subject_list'),
    # other URLs specific to SubjectDetail
]