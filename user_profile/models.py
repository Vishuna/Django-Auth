from django.db import models

# Create your models here.
def get_default_image():
    return 'static/media/images/user.png'
class UserProfile(models.Model):
    ROLE_CHOICES=(
        ('admin','admin'),
        ('staff','staff'),
        ('student','student'),
    )
    GENDER=(
        ('male','male'),
        ('female','female'),

    )
    ATTENDANCE=(
        ('present','present'),
        ('absent','absent'),
        ('leave','leave')
    )

    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    date_of_birth=models.DateField(blank=True)
    address=models.CharField(max_length=150,blank=True)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,blank=True)
    contact=models.CharField(max_length=15,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER,blank=True)
    attendance=models.CharField(max_length=10,choices=ATTENDANCE,blank=True)
    user_img=models.ImageField(upload_to='static/media/images/',default=get_default_image,blank=True)
    
    def __str__(self):
        return self.first_name



class Student(models.Model):
    GENDER=(
        ('male','male'),
        ('female','female'),
    )
    name=models.CharField(max_length=30,blank=True)
    roll_no=models.CharField(max_length=30,blank=True)
    address=models.CharField(max_length=100,blank=True)
    city=models.CharField(max_length=30,blank=True)
    country=models.CharField(max_length=30,blank=True)
    contact=models.CharField(max_length=15,blank=True)
    gender=models.CharField(max_length=30,blank=True,choices=GENDER)
    st_img=models.ImageField(upload_to='static/media/images/',default=get_default_image,blank=True)

    def __str__(self):
        return self.name 
