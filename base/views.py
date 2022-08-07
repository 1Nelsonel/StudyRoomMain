from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def course(request):
    context = {}
    return render(request,'base/course.html', context)

def community(request):
    context = {}
    return render(request, 'base/community.html', context)

def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)