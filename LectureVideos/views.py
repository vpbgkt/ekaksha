from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from LectureVideos.models import lecturevideos

class lecturevideosListView(ListView):
    model = lecturevideos
    template_name = 'pages/subjectvideos.html'
    context_object_name = 'lecturelist'

class lecturevideosDetailView(DetailView):
    model = lecturevideos
    template_name = 'pages/subjectvideos.html'
    context_object_name = 'lecturevideo'










# from django.shortcuts import render, get_object_or_404
# from LectureVideos.models import lecturevideos
# from SubjectDetail.models import Subjects

# def lectures(request, subject_id):
#     subject = get_object_or_404(Subjects, pk=subject_id)
#     videos = lecturevideos.objects.filter(Subjects=subject)
#     # fetch the video_url of each Video object
#     video_urls = [video.video_url for video in videos if video.video_url]
#     context = {'subject': subject, 'videos': videos, 'video_urls': video_urls}
#     return render(request, 'pages/subjectvideos.html', context)


# ORIGINAL CODE
# def subject_videos(request, subject_id):
#     subject = get_object_or_404(Subjects, pk=subject_id)
#     videos = Video.objects.filter(Subjects=subject)
#     # fetch the video_url of each Video object
#     video_urls = [video.video_url for video in videos if video.video_url]
#     context = {'subject': subject, 'videos': videos, 'video_urls': video_urls}
#     return render(request, 'pages/subjectvideos.html', context)
