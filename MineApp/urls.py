from django.conf.urls import url

from MineApp import views

urlpatterns = [
    # app的个人中心页面
    url(r'^mine/', views.mine, name='mine')
]
