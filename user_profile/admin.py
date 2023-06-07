from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','date_of_birth')
    list_filter=('first_name','role')
    search_fields=('last_name',)
    ordering=('first_name',)

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','roll_no','address','contact')
