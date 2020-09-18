import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from UserApp.models import User, Address
from libs.utils import login_required, send_email


# 登录
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


# 注册检查
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


# 账号激活
def be_active(request):
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


# 注册
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


# 修改信息检查
@login_required
def update_check(request):
    username = request.session.get('username')

    # 判断邮箱
    email = request.GET.get('email')
    email_num = User.objects.filter(userEmail=email).count()
    if email_num == 1:
        email_owner_name = User.objects.filter(userEmail=email)[0].userName
        if email_owner_name != username:
            data = {
                'msg': '邮箱已被绑定或有误！'
            }
            return JsonResponse(data)
        else:
            data = {
                'msg': 'ok'
            }
            return JsonResponse(data)
    elif email_num == 0:
        data = {
            'msg': 'ok'
        }
        return JsonResponse(data)

    # 判断手机
    phone = request.GET.get('phone')
    phone_num = User.objects.filter(userPhone=phone).count()
    if phone_num == 1:
        phone_owner_name = User.objects.filter(userPhone=phone)[0].userName
        if phone_owner_name != username:
            data = {
                'msg': '手机号已被绑定或有误！'
            }
            return JsonResponse(data)
        else:
            data = {
                'msg': 'ok'
            }
            return JsonResponse(data)
    elif phone_num == 0:
        data = {
            'msg': 'ok'
        }
        return JsonResponse(data)


# 用户信息
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
        user = User.objects.filter(userName=username)[0]

        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # 判断头像
        img_url = request.FILES.get('header', '')
        if not img_url:
            img_url = user.userImg

        # 新密码
        password = request.POST.get('password', '')
        if password:
            # 加密
            salt = 'asfeg'
            password = make_password(password, salt, 'pbkdf2_sha1')
        else:
            password = user.userPasswd

        user.nickName = nickname
        user.userPasswd = password
        user.userPhone = phone
        user.userEmail = email
        user.userImg = img_url
        user.save()
        return redirect(reverse('blmmine:mine'))


# 用户地址
@login_required
def address(request):
    username = request.session.get('username')
    user = User.objects.filter(userName=username)[0]

    if request.method == "GET":
        addr_id = request.GET.get('addr_id', '')
        if addr_id:
            addr_used_num = Address.objects.filter(userId=user.id).filter(isselect=1).count()
            # 如果没有默认地址，设置它为默认地址
            if addr_used_num == 0:
                addr_used = Address.objects.get(pk=addr_id)
                addr_used.isselect = True
                addr_used.save()

                addrs = Address.objects.filter(userId=user.id).exclude(pk=addr_used.id)
                context = {
                    'addrs': addrs,
                    'addr_used': addr_used,
                }
                return render(request, 'blm/user/address.html', context=context)
            # 如果有默认地址，设置它为默认地址，把旧的地址改为非默认
            else:
                addr_old_used = Address.objects.filter(userId=user.id).filter(isselect=1)[0]
                addr_old_used.isselect = False
                addr_old_used.save()

                addr_used = Address.objects.get(pk=addr_id)
                addr_used.isselect = True
                addr_used.save()

                addrs = Address.objects.filter(userId=user.id).exclude(pk=addr_used.id)
                context = {
                    'addrs': addrs,
                    'addr_used': addr_used,
                }
                return render(request, 'blm/user/address.html', context=context)
        else:
            # 判断是否有默认
            addr_used_num = Address.objects.filter(userId=user.id).filter(isselect=1).count()
            if addr_used_num == 0:
                addrs = Address.objects.filter(userId=user.id)
                context = {
                    'addrs': addrs,
                }
                return render(request, 'blm/user/address.html', context=context)
            else:
                addr_used = Address.objects.filter(userId=user.id).filter(isselect=1)[0]
                addrs = Address.objects.filter(userId=user.id).exclude(pk=addr_used.id)
                context = {
                    'addrs': addrs,
                    'addr_used': addr_used,
                }
                return render(request, 'blm/user/address.html', context=context)

    else:
        consignee = request.POST.get('consignee')
        userPhone = request.POST.get('phone')
        detailAdd = request.POST.get('address')

        addr = Address(userId=user.id, consignee=consignee, userPhone=userPhone, detailAdd=detailAdd)
        addr.save()
        return redirect(reverse('user:address'))


# 退出
def logout(request):
    # 删除session
    request.session.flush()
    return redirect(reverse('blmmine:mine'))
