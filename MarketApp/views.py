from django.http import JsonResponse
from django.shortcuts import render

from CarApp.models import BlmCar
from MarketApp.models import BlmFoodType, BlmGoods, BlmOrderType
from UserApp.models import User
from libs.utils import login_required


def market(request):
    # 获取全部种类
    foodtypes = BlmFoodType.objects.all()

    # 根据种类id进行第一次查询
    typeid = request.GET.get('typeid', '104749')
    good_list = BlmGoods.objects.filter(categoryid=typeid)

    foodtype = BlmFoodType.objects.filter(typeid=typeid)[0]
    childtypename = foodtype.childtypenames
    child_list = childtypename.split('#')

    child_name_list = []
    for child in child_list:
        child_name = child.split(':')
        child_name_list.append(child_name)

    # 根据分类id进行第二次查询
    childcid = request.GET.get('childcid', '0')
    if childcid == '0':
        pass
    else:
        good_list = good_list.filter(childcid=childcid)

    # 根据排序类型进行第三次查询
    # 1-5 分别是 默认 价格升序、降序 销量升序、降序
    ordertypes = BlmOrderType.objects.all()

    orderid = int(request.GET.get('ordertype', 1))
    if orderid == 1:
        pass
    elif orderid == 2:
        good_list = good_list.order_by('price')
    elif orderid == 3:
        good_list = good_list.order_by('-price')
    elif orderid == 4:
        good_list = good_list.order_by('productnum')
    elif orderid == 5:
        good_list = good_list.order_by('-productnum')

    context = {
        'foodtypes': foodtypes,
        'good_list': good_list,
        'child_name_list': child_name_list,
        'typeid': typeid,
        'childcid': childcid,
        'orderid': orderid,
        'ordertypes': ordertypes,
    }

    return render(request, 'blm/main/market/market.html', context=context)


def good_num(request):
    username = request.session.get('username')
    g_id = request.GET.get('g_id')
    u_id = User.objects.filter(userName=username)[0].id

    car_num = BlmCar.objects.filter(g_id=g_id, u_id=u_id).count()
    if car_num == 0:
        data = {
            'g_num': 0
        }
        return JsonResponse(data)
    else:
        car = BlmCar.objects.filter(g_id=g_id, u_id=u_id)[0]
        g_num = car.g_num
        data = {
            'g_num': g_num
        }
        return JsonResponse(data)
