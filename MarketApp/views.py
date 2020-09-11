from django.shortcuts import render

# Create your views here.
from MarketApp.models import BlmFoodType, BlmGoods


def market(request):
    foodtypes = BlmFoodType.objects.all()
    goods1 = BlmGoods.objects.filter(categoryid='104749')[0:4]
    goods2 = BlmGoods.objects.filter(categoryid='104747')[0:4]
    goods3 = BlmGoods.objects.filter(categoryid='103532')[0:4]
    goods4 = BlmGoods.objects.filter(categoryid='103581')[0:4]
    goods5 = BlmGoods.objects.filter(categoryid='103536')[0:4]
    goods6 = BlmGoods.objects.filter(categoryid='103549')[0:4]
    goods7 = BlmGoods.objects.filter(categoryid='103541')[0:4]
    goods8 = BlmGoods.objects.filter(categoryid='103557')[0:4]
    goods9 = BlmGoods.objects.filter(categoryid='103569')[0:4]
    goods10 = BlmGoods.objects.filter(categoryid='103575')[0:4]
    goods11 = BlmGoods.objects.filter(categoryid='104958')[0:4]

    context = {
        'foodtypes': foodtypes,
        'goods1': goods1,
        'goods2': goods2,
        'goods3': goods3,
        'goods4': goods4,
        'goods5': goods5,
        'goods6': goods6,
        'goods7': goods7,
        'goods8': goods8,
        'goods9': goods9,
        'goods10': goods10,
        'goods11': goods11,
    }

    return render(request, 'blm/main/market/market.html', context=context)
