import re

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from UserApp.models import User
from libs.utils import login_required


def login(request):
    if request.method == "GET":
        return render(request, 'blm/user/login.html')
    else:
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        # 判断用户是否存在
        user_num = User.objects.filter(userName=username).count()
        if user_num == 0 or re.search(r'^[a-zA-Z0-9_-]{6,12}$', username) is None:
            return JsonResponse({'msg': '用户名有误！'})

        # 解密
        user = User.objects.filter(userName=username)[0]
        if not check_password(password, user.userPasswd) or re.search(r'^[a-zA-Z0-9_-]{6,12}$', password) is None:
            return JsonResponse({'msg': '密码有误！'})

        # 设置session 登录成功
        request.session['username'] = username

        return redirect(reverse('blmmine:mine'))


def register(request):
    if request.method == "GET":
        return render(request, 'blm/user/register.html')
    else:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        c_password = data.get('c_password')
        userphone = data.get('phone')
        email = data.get('email')

        # 判断密码
        if (not password) or (c_password != password):
            return JsonResponse({'msg': '密码有误！'})

        # 判断用户名
        user_num = User.objects.filter(userName=username).count()
        if (user_num == 1) or re.search(r'^[a-zA-Z0-9_-]{6,12}$', username) is None:
            return JsonResponse({'msg': '用户名已存在或有误！'})

        # 判断手机
        phone_num = User.objects.filter(userPhone=userphone).count()
        if phone_num == 1 or re.search(r'^1[34578]\d{9}$', userphone) is None:
            return JsonResponse({'msg': '手机号已被绑定或有误！'})

        # 判断邮箱
        email_num = User.objects.filter(userEmail=email).count()
        if email_num == 1 or re.search(r'^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$',
                                       email) is None:
            return JsonResponse({'msg': '邮箱已被绑定或有误！'})

        # 加密
        salt = 'asfeg'
        new_password = make_password(password, salt, 'pbkdf2_sha1')
        # 创建用户
        user = User(userName=username, userPasswd=new_password, userPhone=userphone, userEmail=email)
        user.save()
        return redirect(reverse('user:login'))


@login_required
def user_info(request):
    if request.method == "GET":
        username = request.session.get('username')

        user = User.objects.filter(userName=username)[0]
        context = {
            'user': user,
        }
        return render(request, 'blm/user/user_info.html', context=context)

    else:
        username = request.session.get('username')
        nickname = request.POST.get('nickname', '')

        # 判断手机
        phone = request.POST.get('phone', '')
        if re.search(r'^1[34578]\d{9}$', phone) is None:
            return redirect(reverse('user:userinfo'))

        phone_num = User.objects.filter(userPhone=phone).count()
        if phone_num == 1:
            phone_owner_name = User.objects.filter(userPhone=phone)[0].userName
            if phone_owner_name != username:
                return redirect(reverse('user:userinfo'))

        # 判断邮箱
        email = request.POST.get('email', '')
        if re.search(r'^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$', email) is None:
            return redirect(reverse('user:userinfo'))

        email_num = User.objects.filter(userEmail=email).count()
        if email_num == 1:
            email_owner_name = User.objects.filter(userEmail=email)[0].userName
            if email_owner_name != username:
                return redirect(reverse('user:userinfo'))

        # 判断旧密码
        user = User.objects.filter(userName=username)[0]
        old_password = request.POST.get('old_password', '')
        if not check_password(old_password, user.userPasswd):
            return redirect(reverse('user:userinfo'))

        # 判断头像
        img_url = request.FILES.get('header', '')
        if not img_url:
            img_url = user.userImg

        # 判断新密码
        password = request.POST.get('password', '')
        c_password = request.POST.get('c_password', '')
        if password:
            if re.search(r'^[a-zA-Z0-9_-]{6,12}$', password) is None:
                return redirect(reverse('user:userinfo'))

            if c_password != password:
                return redirect(reverse('user:userinfo'))
        else:
            password = old_password

        # 加密
        salt = 'asfeg'
        new_pwd = make_password(password, salt, 'pbkdf2_sha1')

        user.nickName = nickname
        user.userPasswd = new_pwd
        user.userPhone = phone
        user.userImg = img_url
        user.save()
        return redirect(reverse('blmmine:mine'))


def logout(request):
    # 删除session
    request.session.flush()
    return redirect(reverse('blmmine:mine'))
