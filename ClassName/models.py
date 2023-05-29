from django.db import models

class ClassName(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    class_image = models.ImageField(upload_to='uploads/class_images/', null=True, blank=True)
    