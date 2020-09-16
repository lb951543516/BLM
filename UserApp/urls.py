from django.conf.urls import url

from UserApp import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),

    # 注册
    url(r'^register/', views.register, name='register'),

    # 注册检查
    url(r'^regcheck/', views.reg_check, name='regcheck'),

    # 邮箱，帐号激活
    url(r'^beactive/', views.beactive, name='beactive'),

    # 个人资料
    url(r'^userinfo/', views.user_info, name='userinfo'),

    # 地址管理
    url(r'^address/', views.address, name='address'),

    # 退出
    url(r'^logout/', views.logout, name='logout'),
]
