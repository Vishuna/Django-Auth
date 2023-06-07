from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('',views.base,name="base"),
    path('profile/',views.user_profile,name='user_profile'),
    path('view_profile/',views.view_profile,name="view_profile"),
    path('student/',views.student,name="student"),
]