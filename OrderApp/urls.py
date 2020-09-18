from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    # 产生订单
    url(r'^order/', views.order, name='order'),

    # 查看你的订单详情
    url(r'^orderinfo/', views.order_info, name='orderinfo'),
]
