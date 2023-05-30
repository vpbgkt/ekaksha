"""
URL configuration for Ekaksha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from Ekaksha import settings, views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('ClassName/', include('ClassName.urls')),
    path('Subjects/', include('SubjectDetail.urls')),
    



    path('aboutus/', views.aboutus, name='aboutus'),
    # path('ClassName/', include('ClassName.urls')),
    # path('Classes/', views.eclass_list, name='eclass_list'),
    # path('subject/', views.subject, name='subject'),
    
    # path('subject/<subject_id>/', views.subject_videos, name='subject_videos'),
    # path('eclass_list/<int:eclass_id>/', name='subjects'),
    # path('Classes/<str:class_name>/',views.subject, name='eclass_list'),
    path('contect/', views.contect, name='contect'),
    # path('signup', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # New
