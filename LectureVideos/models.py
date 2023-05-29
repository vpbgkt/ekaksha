from django.db import models
from SubjectDetail.models import Subjects

class lecturevideos(models.Model):
    title = models.CharField(max_length=100)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    video_url = models.URLField(null=True,blank=True)
    description = models.TextField()
    video_file = models.FileField(upload_to='uploads/videos/',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/',null=True,blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    duration_mint = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title