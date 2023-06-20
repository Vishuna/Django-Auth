from django.urls import path
from . import views
from .views import *

urlpatterns=[
 
    path('download/',views.download_video,name="download_video"),
    path('videos/',views.video_view,name="view_videos"),
]