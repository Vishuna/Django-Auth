from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordResetView



def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            print(user)
            user.save()
            
            current_site=get_current_site(request)
            mail_subject="Activation Link has been sent to your id"
            message=render_to_string('registration/acc_active_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),

            })
            to_email=form.cleaned_data.get('email')
            print(to_email)
            email=EmailMessage(
                mail_subject,message,to=[to_email]

            )
            email.send()
            print("yes")
            return HttpResponse('Please Confirm your email address to complete the registration')
    else:
            print("test")
            form=SignupForm()
    return render(request,'registration/register.html',{'form':form})
    
def activate(request,uidb64,token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
        print(user)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        return HttpResponse("Thank your for your email confirmation!")
    else:
        return HttpResponse("Activation link is valid!")


def user_profile(request):
    return render(request,'registration/profile.html')











