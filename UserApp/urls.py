from django.conf.urls import url

from UserApp import views

urlpatterns = [

    # 登录
    url(r'^login/', views.login, name='login'),

    # 注册
    url(r'^register/', views.register, name='register'),
]
