from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import *

urlpatterns = [
    # path('profile/',views.profile,name="profile"),
    path('userprofile/',views.user_profile, name="user_profile"),
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('register/',views.register,name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate,name="activate"),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm"),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name="password_reset_complete"),
    
    
    
]