from django.shortcuts import render

# Create your views here.

def account(request):
    context = {}
    return render(request, 'account/login-signin.html', context)
