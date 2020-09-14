from django.conf.urls import url

from UserApp import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),

    # 注册
    url(r'^register/', views.register, name='register'),

    # 个人资料
    url(r'^userinfo/', views.userinfo, name='userinfo'),

    # 退出
    url(r'^logout/', views.logout, name='logout'),
]
