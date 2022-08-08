from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import Blog, Category, Comment

# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/home.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def course(request):
    context = {}
    return render(request, 'base/course.html', context)


def community(request):
    context = {}
    return render(request, 'base/community.html', context)


def contact(request):
    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.POST.get('user'),
            subject=request.POST.get('subject'),
            email=request.POST.get('email'),
            body=request.POST.get('body'),
        )

        messages.success(request, 'Message sent')
        return redirect('contact')
    context = {}
    return render(request, 'base/contact.html', context)


def blog(request):
    categories = Category.objects.all()
    comments = Comment.objects.all()
    blogs = Blog.objects.all()
    context = {'blogs': blogs, 'categories': categories, 'comments': comments}
    return render(request, 'base/blog.html', context)


def blogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    blogs = Blog.objects.all()
    comments = blog.comment_set.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            blog=blog,
            user=request.POST.get('user'),
            email=request.POST.get('email'),
            body=request.POST.get('body'),
        )

        messages.success(request, 'Message sent')
        return redirect('blogDetail', pk=blog.id)
    context = {'blog': blog, 'comments': comments, 'blogs': blogs}
    return render(request, 'base/blog-single.html', context)
