from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    
    class Meta:
        model=Student
        fields=['name','roll_no','address','city','country','contact','st_img','gender']

        
    # gender_t=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))


    # If i want to enable multiple file selection with a clearable file input you can use a third party library like
    # "django-widget-tweaks" // pip install django-wideget-tweaks
