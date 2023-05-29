from django.contrib import admin
from SubjectDetail.models import Subjects

class SubjectDetailAdmin(admin.ModelAdmin):
    list_display=('name','title','instructure_name','description','class_name','subject_image','updated_on')

admin.site.register(Subjects,SubjectDetailAdmin)
