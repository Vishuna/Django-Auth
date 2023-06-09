from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm
from templates import *
from .models import *
from datetime import datetime

from django.core.paginator import Paginator

# Create your views here.


def base(request):
    return render(request,'base.html')

def user_profile(request):
    if request.method=="POST":
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        role=request.POST.get('role')
        gender=request.POST.get('gender')
        attendance=request.POST.get('attendance')
        img_upload=request.FILES['imgUpload']
        print(img_upload)

        userProfile=UserProfile()
        userProfile.first_name=first_name
        userProfile.last_name=last_name
        userProfile.address=address
        userProfile.contact=contact
        userProfile.role=role
        userProfile.gender=gender
        userProfile.attendance=attendance
        userProfile.user_img=img_upload
        date=datetime.strptime(dob,'%m-%d-%Y')
        formatted_date=date.strftime("%Y-%m-%d")
        userProfile.date_of_birth=formatted_date

        userProfile.save()

    return render(request,'user_profile/user_profile.html')


def view_profile(request):
    users_data=UserProfile.objects.all()
    paginator=Paginator(users_data,3)
    page_number=request.GET.get('page')
    page=paginator.get_page(page_number)
    context={
        'users_data':users_data,
        'page':page,
    }
    for i in users_data:
        print(i.user_img)
    return render(request,'user_profile/view_profile.html',context)

def student(request):
    if request.method=='POST':
        student_form=StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponse('success')
            # name=student_form.cleaned_data['name']
            # roll_no=student_form.cleaned_data['roll_no']
            # address=student_form.cleaned_data['address']
            # city=student_form.cleaned_data['city']
            # country=student_form.cleaned_data['country']
            # gender=student_form.cleaned_data['gender']
            # st_img=student_form.cleaned_data['st_img']
    else:


        student_form=StudentForm()

        context={
        'forms':student_form,
        }

    return render(request,'student/student_form.html',context)
