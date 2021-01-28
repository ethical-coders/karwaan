from django.shortcuts import render
from .models import Blog
#from django.views.generic import ListView, DetailView


# Create your views here.

def index(request):
    
    
    blog1 = Blog()
    blog1.person='Palak Shivlani'
    blog1.name='Social Media feed: A hoax or reality?'
    blog1.desc='As I write about it , I have no clue how to put all my ideas regarding different perspective in a single page but nevermind, In order to get you familiar with my point of view I have done my bit .'
    blog1.image='blog1.jpg'

    blog2 = Blog()
    blog2.person='Parmeshwar Sahu'
    blog2.name='Future of Devices:IOT'
    blog2.desc='The internet of things is a rapidly growing technology which aims to connect all devices to the existing Internet infrastructure.'
    blog2.image='iot4.jpeg'

    blogs = [blog1 , blog2]

    #print(blogs)
    return render(request,'index.html',{'blogs' : blogs});

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

#class IndexView(ListView):
    #model=Blog
    #template_name='index.html'

def blog1(request):
    return render(request,'blog-single.html')

def blog2(request):
    return render(request,'iot.html')
