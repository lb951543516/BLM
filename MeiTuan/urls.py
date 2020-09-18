"""MeiTuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 饱了吗App的首页面
    url(r'^blmhome/', include('HomeApp.urls', namespace='blmhome')),

    # 饱了吗App的个人页面
    url(r'^blmmine/', include('MineApp.urls', namespace='blmmine')),

    # 饱了吗App的购物车页面
    url(r'^blmcar/', include('CarApp.urls', namespace='blmcar')),

    # 饱了吗App的分类购买页面
    url(r'^blmmarket/', include('MarketApp.urls', namespace='blmmarket')),

    # 饱了吗用户页面
    url(r'^user/', include('UserApp.urls', namespace='user')),

    # 饱了吗订单页面
    url(r'^blmorder/', include('OrderApp.urls', namespace='blmorder')),
]
