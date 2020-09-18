from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from CarApp.models import BlmCar
from UserApp.models import User

from libs.utils import check_addr, pay_money


# 购物车页面
def car(request):
    username = request.session.get('username')
    u_id = User.objects.filter(userName=username)[0].id
    cars = BlmCar.objects.filter(c_user_id=u_id)

    # 如果当前用户的购物车里 不存在 有未选择 的商品------true代表全都选择了 ,false代表没有全部都选
    is_all_buy = not BlmCar.objects.filter(c_user_id=u_id).filter(is_buy=False).exists()

    # 检查是否设置了默认地址
    can_pay = False
    if check_addr(request):
        can_pay = True
    else:
        can_pay = False

    context = {
        'cars': cars,
        'money': pay_money(request),
        'can_pay': can_pay,
        'u_id': u_id,
        'is_all_buy': is_all_buy
    }

    return render(request, 'blm/main/car/car.html', context=context)


# 全球购页面添加商品
def addtocar(request):
    username = request.session.get('username')
    g_id = request.GET.get('g_id')
    u_id = User.objects.filter(userName=username)[0].id

    car_num = BlmCar.objects.filter(c_good_id=g_id).filter(c_user_id=u_id).count()
    if car_num == 0:
        car = BlmCar(c_user_id=u_id, c_good_id=g_id, g_num=1)
        car.save()
        data = {
            'g_num': car.g_num,
        }
        return JsonResponse(data)
    elif car_num > 0:
        car = BlmCar.objects.filter(c_good_id=g_id).filter(c_user_id=u_id)[0]
        car.g_num += 1
        car.save()
        data = {
            'g_num': car.g_num,
        }
        return JsonResponse(data)


# 全球购页面减少商品
def reducetocar(request):
    username = request.session.get('username')
    g_id = request.GET.get('g_id')
    u_id = User.objects.filter(userName=username)[0].id

    car_num = BlmCar.objects.filter(c_good_id=g_id).filter(c_user_id=u_id).count()
    if car_num == 0:
        data = {
            'g_num': 0,
        }
        return JsonResponse(data)
    elif car_num == 1:
        car = BlmCar.objects.filter(c_good_id=g_id).filter(c_user_id=u_id)[0]
        if car.g_num > 1:
            car.g_num -= 1
            car.save()
            data = {
                'g_num': car.g_num,
            }
            return JsonResponse(data)
        elif car.g_num == 1:
            car.delete()
            data = {
                'g_num': 0,
            }
            return JsonResponse(data)


# 购物车页面减少商品
def reducegood(request):
    c_id = request.GET.get('c_id')

    car = BlmCar.objects.get(pk=c_id)
    if car.g_num > 1:
        car.g_num -= 1
        car.save()

        data = {
            'g_num': car.g_num,
            'money': pay_money(request),
        }
        return JsonResponse(data)
    elif car.g_num == 1:
        car.delete()
        data = {
            'g_num': 0,
            'money': pay_money(request),
        }
        return JsonResponse(data)


# 购物车页面增加商品
def addgood(request):
    c_id = request.GET.get('c_id')

    car = BlmCar.objects.get(pk=c_id)
    car.g_num += 1
    car.save()

    data = {
        'g_num': car.g_num,
        'money': pay_money(request),
    }
    return JsonResponse(data)


# 删除购物车内的商品
def deletegood(request):
    cid = request.GET.get('cid')
    car = BlmCar.objects.get(pk=cid)
    car.delete()
    return redirect(reverse('blmcar:car'))


# 结算
def pay(request):
    uid = request.GET.get('uid')
    car_num = BlmCar.objects.filter(c_user_id=uid).filter(is_buy=True).count()
    if car_num > 0:
        cars = BlmCar.objects.filter(c_user_id=uid).filter(is_buy=True)
        cars.delete()

        return redirect(reverse('user:order'))
    else:
        return redirect(reverse('blmcar:car'))


# 改变单选框的状态
def changeStatus(request):
    c_id = request.POST.get('c_id')

    car = BlmCar.objects.get(pk=c_id)

    car.is_buy = not car.is_buy

    car.save()

    username = request.session.get('username')
    u_id = User.objects.filter(userName=username)[0].id

    # 如果当前用户的购物车里 不存在 有未选择 的商品------true代表全都选择了 ,false代表没有全部都选
    is_all_buy = not BlmCar.objects.filter(c_user_id=u_id).filter(is_buy=False).exists()

    data = {
        'car.is_buy': car.is_buy,
        'is_all_buy': is_all_buy,
        'money': pay_money(request),
    }
    return JsonResponse(data=data)


def allselect(request):
    # ajax的参数不能传递列表---以#连接字符串传递过来
    c_id_list = request.GET.get('c_id_list')
    # 以#切割字符串变成列表
    id_list = c_id_list.split('#')

    car_list = BlmCar.objects.filter(id__in=id_list)

    for car in car_list:
        car.is_buy = not car.is_buy
        car.save()

    data = {
        'msg': 'ok',
        'status': 200,
        'money': pay_money(request),
    }
    return JsonResponse(data=data)
