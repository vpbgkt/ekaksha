from django.shortcuts import render, get_object_or_404
from LectureVideos.models import lecturevideos
from SubjectDetail.models import Subjects

def lectures(request, subject_id):
    subject = get_object_or_404(Subjects, pk=subject_id)
    videos = lecturevideos.objects.filter(Subjects=subject)
    # fetch the video_url of each Video object
    video_urls = [video.video_url for video in videos if video.video_url]
    context = {'subject': subject, 'videos': videos, 'video_urls': video_urls}
    return render(request, 'pages/subjectvideos.html', context)


# ORIGINAL CODE
# def subject_videos(request, subject_id):
#     subject = get_object_or_404(Subjects, pk=subject_id)
#     videos = Video.objects.filter(Subjects=subject)
#     # fetch the video_url of each Video object
#     video_urls = [video.video_url for video in videos if video.video_url]
#     context = {'subject': subject, 'videos': videos, 'video_urls': video_urls}
#     return render(request, 'pages/subjectvideos.html', context)
