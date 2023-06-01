from django.db import models

# Abstract Model Inheritance

class ContactInfo(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=30)

    class Meta:
        abstract=True

    
class Customer(ContactInfo):
    phone=models.CharField(max_length=30)


class Staff(ContactInfo):
    position=models.CharField(max_length=100)



# MultiTable Model Inheritance

class Place(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)

    def _str__(self):
        return self.name

class Restaurant(Place):
    soups=models.BooleanField(default=False)
    pizza=models.BooleanField(default=False)

    def __str__(self):
        return self.soups
    


# Proxy Model Inheritance


class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    
class MyPerson(Person):
    class Meta:
        proxy=True
        ordering=['first_name']



# Polymorphism

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()


class Comment(models.Model):
    text= models.TextField()
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='replies')
    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,related_name='comments'
    )

    # Retrieve all the elements associated with a post

post=Post.obejcts.get(id=1)
comments=post.comments.all()

    # Retrieve all replies to a comment

comment =Comment.objects.all(id=1)
replies=comment.replies.all()

    # Encapsulation

from django.contrib.auth.models import User

class Post(models.Model):
        title=models.CharField(max_length=100)
        content=models.TextField()
        author=models.ForeignKey(User,on_delete=models.CASCADE)
        publication_date=models.DateTimeField(auto_now_add=True)


# Post.objects.filter(author=user)

class Post(models.Model):
    def comment_count(self):
        return self.comments.count()


# Abstraction

# Process of simplyfing complex functionality by hiding unnecessary deatils and providing a simplified interface to work with.
# It alllows you to focus on the essentil aspects of your application while abstracting away the underlying implemenation complexities.

# Serveral Abstraction that help you build web applications:
# 1. URL Patterns
# 2. ORM(Object-Relational Mapping)
# 3. Template Language
# 4. Forms
# 5. MiddleWare

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=0,decimal_places=2)
    description= models.TextField()

    # Querying the Database:

from .models import Product

def get_all_products():
    return Product.objects.all()

from django.shortcuts import render
from .utils import get_all_products

def product_list(request):
    products=get_all_products()
    return render(request,'product_list.html',{'products':products})


# product_list.html

{% for product in products %}
<div class="product">
    <h3>{{product.name}}</h3>
    <p>{{product.price}}</p>
    <p>{{product.description}}</p>
</div>
{% endfor %}


# By utilizing these abstraction, you can work with higer-level concept such as models, views and templates.
# It simplifies the development process, promotes code maintainability and allows you to focus on the essential aspects of your application.
