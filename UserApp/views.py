import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from UserApp.models import User, Address
from libs.utils import login_required, send_email


def login(request):
    if request.method == "GET":
        return render(request, 'blm/user/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 判断用户是否存在
        user_num = User.objects.filter(userName=username).count()
        user = User.objects.filter(userName=username)[0]
        if user_num == 1 and check_password(password, user.userPasswd):
            if user.active:
                # 设置session 登录成功
                request.session['username'] = username
                return redirect(reverse('blmmine:mine'))
            else:
                context = {
                    'error': 1
                }
            return render(request, 'blm/user/login.html', context=context)

        else:
            context = {
                'error': 0
            }
            return render(request, 'blm/user/login.html', context=context)


def reg_check(request):
    username = request.POST.get('username', '')
    userphone = request.POST.get('phone', '')
    email = request.POST.get('email', '')

    # 判断用户名
    if username:
        user_num = User.objects.filter(userName=username).count()
        if user_num == 1:
            data = {
                'msg': '用户名已存在或有误！'
            }
            return JsonResponse(data)
        elif user_num == 0:
            data = {
                'msg': 'ok'
            }
            return JsonResponse(data)

    # 判断手机
    if userphone:
        phone_num = User.objects.filter(userPhone=userphone).count()
        if phone_num == 1:
            data = {
                'msg': '手机号已被绑定或有误！'
            }
            return JsonResponse(data)
        elif phone_num == 0:
            data = {
                'msg': 'ok'
            }
            return JsonResponse(data)

    # 判断邮箱
    if email:
        email_num = User.objects.filter(userEmail=email).count()
        if email_num == 1:
            data = {
                'msg': '邮箱已被绑定或有误！'
            }
            return JsonResponse(data)
        elif email_num == 0:
            data = {
                'msg': 'ok'
            }
            return JsonResponse(data)


def beactive(request):
    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:
        user = User.objects.get(pk=user_id)
        user.active = True
        user.save()

        # 激活成功后，删除cache
        cache.delete(token)

        return HttpResponse('激活成功！')
    else:
        return HttpResponse('邮件已过期，请重新发送邮件！')


def register(request):
    if request.method == "GET":
        return render(request, 'blm/user/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        userphone = request.POST.get('phone')
        email = request.POST.get('email')

        # 创建token
        u_token = uuid.uuid4()

        # 加密
        salt = 'asfeg'
        new_password = make_password(password, salt, 'pbkdf2_sha1')

        # 创建用户
        user = User(userName=username, userPasswd=new_password,
                    userPhone=userphone, userEmail=email, userToken=u_token)
        user.save()

        # 发送邮件进行帐号激活
        send_email(username, user.userRank, u_token, email)

        # 设置缓存--来设置邮件的使用时间,,(k,v,时间)
        cache.set(u_token, user.id, timeout=30)

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
        phone = request.POST.get('phone')
        phone_num = User.objects.filter(userPhone=phone).count()
        if phone_num == 1:
            phone_owner_name = User.objects.filter(userPhone=phone)[0].userName
            if phone_owner_name != username:
                return redirect(reverse('user:userinfo'))

        # 判断邮箱
        email = request.POST.get('email')
        email_num = User.objects.filter(userEmail=email).count()
        if email_num == 1:
            email_owner_name = User.objects.filter(userEmail=email)[0].userName
            if email_owner_name != username:
                return redirect(reverse('user:userinfo'))

        # 判断旧密码
        user = User.objects.filter(userName=username)[0]
        old_password = request.POST.get('old_password')
        if not check_password(old_password, user.userPasswd):
            return redirect(reverse('user:userinfo'))

        # 判断头像
        img_url = request.FILES.get('header', '')
        if not img_url:
            img_url = user.userImg

        # 判断新密码
        password = request.POST.get('password', '')
        if password:
            pass
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


@login_required
def address(request):
    username = request.session.get('username')
    user = User.objects.filter(userName=username)[0]

    if request.method == "GET":
        addrs = Address.objects.filter(userId=user.id)
        context = {
            'addrs': addrs
        }
        return render(request, 'blm/user/address.html', context=context)

    else:
        consignee = request.POST.get('consignee')
        userPhone = request.POST.get('phone')
        detailAdd = request.POST.get('address')

        addr = Address(userId=user.id, consignee=consignee, userPhone=userPhone, detailAdd=detailAdd)
        addr.save()
        return redirect(reverse('user:address'))


def logout(request):
    # 删除session
    request.session.flush()
    return redirect(reverse('blmmine:mine'))
