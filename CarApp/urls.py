from django.conf.urls import url

from CarApp import views

urlpatterns = [
    url(r'^car/', views.car, name='car'),

    # 添加到购物车
    url(r'^addtocar/', views.add_to_car, name='addtocar'),

    # 购物车 减少
    url(r'^reducetocar/', views.reduce_to_car, name='reducetocar'),

    #  减少商品
    url(r'^reducegood/', views.reduce_good, name='reducegood'),

    # 增加商品
    url(r'^addgood/', views.add_good, name='addgood'),

    # 删除商品
    url(r'^deletegood/', views.delete_good, name='deletegood'),

    # 删除商品
    url(r'^pay/', views.pay, name='pay'),

    # 改变单选框状态
    url(r'^changestatus/', views.change_status, name='changestatus'),

    # 全选框
    url(r'^allselect/', views.all_select, name='allselect'),
]
