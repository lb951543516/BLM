from django.conf.urls import url

from MarketApp import views

urlpatterns = [
    url(r'^market/', views.market, name='market'),

    # 显示添加的数量
    url(r'^goodnum/', views.goodnum, name='goodnum'),

]
