from django.contrib import admin
from .models import ClassName

class ClassNameAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'class_image')

admin.site.register(ClassName, ClassNameAdmin)
