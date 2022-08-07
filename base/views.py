from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)