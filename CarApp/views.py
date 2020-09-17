from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from CarApp.models import BlmCar
from UserApp.models import User

# 购物车页面
from libs.utils import check_addr


def car(request):
    username = request.session.get('username')
    u_id = User.objects.filter(userName=username)[0].id
    cars = BlmCar.objects.filter(c_user_id=u_id)

    # 检查是否设置了默认地址
    can_pay = False
    if check_addr(request):
        can_pay = True
    else:
        can_pay = False

    money = 0
    for car in cars:
        if car.is_buy:
            money += car.c_good.price * car.g_num

    context = {
        'cars': cars,
        'money': money,
        'can_pay': can_pay,
        'u_id': u_id,
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
        }
        return JsonResponse(data)
    elif car.g_num == 1:
        car.delete()
        data = {
            'g_num': 0,
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
    cars = BlmCar.objects.filter(c_user_id=uid)
    cars.delete()

    return redirect(reverse('user:order'))
