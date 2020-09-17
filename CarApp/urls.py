from django.conf.urls import url

from CarApp import views

urlpatterns = [
    url(r'^car/', views.car, name='car'),

    # 添加到购物车
    url(r'^addtocar/', views.addtocar, name='addtocar'),

    # 购物车 减少
    url(r'^reducetocar/', views.reducetocar, name='reducetocar'),

    #  减少商品
    url(r'^reducegood/', views.reducegood, name='reducegood'),

    # 增加商品
    url(r'^addgood/', views.addgood, name='addgood'),

    # 删除商品
    url(r'^deletegood/', views.deletegood, name='deletegood'),

    # 删除商品
    url(r'^pay/', views.pay, name='pay'),
]
