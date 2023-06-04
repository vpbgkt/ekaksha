from django.urls import path
from .views import lecturevideosListView, lecturevideosDetailView

app_name = 'LectureVideos'

urlpatterns = [
    path('', lecturevideosListView.as_view(), name='lecturevideos-list'),
    path('course/<int:class_pk>/<int:pk>/', lecturevideosDetailView.as_view(), name='lecturevideos-detail'),
    # other URLs specific to ClassName or the app

]
