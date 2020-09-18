from django.http import HttpResponse
from django.shortcuts import render


# 订单详情
def order(request):
    return render(request, 'blm/order/order.html')
