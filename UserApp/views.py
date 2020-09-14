from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from UserApp.models import User


def login(request):
    if request.method == "GET":
        return render(request, 'blm/user/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 判断用户是否存在
        user_num = User.objects.filter(userName=username).count()
        if user_num == 0:
            context = {
                'error': 1
            }
            return render(request, 'blm/user/login.html', context=context)

        # 解密
        user = User.objects.filter(userName=username)[0]
        if not check_password(password, user.userPasswd):
            context = {
                'error': 0
            }
            return render(request, 'blm/user/login.html', context=context)

        # 设置session 登录成功
        request.session['username'] = username
        return redirect(reverse('blmmine:mine'))


def register(request):
    if request.method == "GET":
        return render(request, 'blm/user/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        userphone = request.POST.get('phone')

        # 判断验证码

        # 判断密码
        if (not password) or (c_password != password) or (not 6 <= len(password) <= 12):
            context = {
                'error': 1
            }
            return render(request, 'blm/user/register.html', context=context)

        # 判断用户名
        user_num = User.objects.filter(userName=username).count()
        if (user_num == 1) or not (6 <= len(username) <= 12):
            context = {
                'error': 0
            }
            return render(request, 'blm/user/register.html', context=context)

        # 判断手机
        phone_num = User.objects.filter(userPhone=userphone).count()
        if phone_num == 1:
            context = {
                'error': 2
            }
            return render(request, 'blm/user/register.html', context=context)

        # 加密
        salt = 'asfeg'
        new_password = make_password(password, salt, 'pbkdf2_sha1')
        # 创建用户
        user = User(userName=username, userPasswd=new_password, userPhone=userphone)
        user.save()
        return redirect(reverse('user:login'))


def userinfo(request):
    if request.method == "GET":
        return render(request, 'blm/user/user_info.html')
    else:
        pass


def logout(request):
    # 删除session
    request.session.flush()
    return redirect(reverse('blmmine:mine'))