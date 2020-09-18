from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from CarApp.models import BlmCar
from OrderApp.models import BlmOrder, Blm_OrderGoods
from UserApp.models import User, Address
from libs.utils import pay_money


# 结算 产生订单
def order(request):
    uid = request.GET.get('uid')
    money = pay_money(request)
    car_num = BlmCar.objects.filter(c_user_id=uid).filter(is_buy=True).count()
    if car_num > 0:
        # 创建 订单
        order = BlmOrder(o_user_id=uid, o_total_price=money)
        order.save()

        # 创建 商品订单
        cars = BlmCar.objects.filter(c_user_id=uid).filter(is_buy=True)
        for car in cars:
            ordergood = Blm_OrderGoods(og_order=order, og_c_good_num=car.g_num, og_good=car.c_good)
            ordergood.save()
            # 订单完成，删除购物车页面购买的物品
            car.delete()

        return redirect(reverse('blmorder:orderinfo'))
    else:
        return redirect(reverse('blmcar:car'))


def order_info(request):
    username = request.session.get('username')
    uid = User.objects.filter(userName=username)[0].id

    addr = Address.objects.filter(userId=uid).filter(isselect=True)[0]
    addr_detail = addr.detailAdd[:15]+'...'

    orders = BlmOrder.objects.filter(o_user_id=uid).order_by('-o_time')
    context = {
        'orders': orders,
        'addr': addr,
        'addr_detail': addr_detail
    }
    return render(request, 'blm/order/order.html', context=context)
