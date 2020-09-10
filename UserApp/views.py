from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

def login(request):
    if request.method == "GET":
        return render(request, 'blm/user/login.html')
    else:
        return HttpResponse('登录成功')


def register(request):
    if request.method == "GET":
        return render(request, 'blm/user/register.html')
    else:
        return redirect(reverse('user:login'))
