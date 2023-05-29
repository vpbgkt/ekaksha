from django.db import models
from ClassName.models import ClassName

class Subjects(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    instructure_name = models.CharField(max_length=50)
    description = models.TextField()
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE,related_name='subjects')
    subject_image = models.ImageField(upload_to='uploads/subject_images/', null=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name