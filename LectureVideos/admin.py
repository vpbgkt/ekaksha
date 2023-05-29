from django.contrib import admin
from .models import lecturevideos
class LectureVideosAdmin(admin.ModelAdmin):
    list_display =('title','subjects','video_url','description','video_file','thumbnail','uploaded_on','duration_mint')

admin.site.register(lecturevideos,LectureVideosAdmin)