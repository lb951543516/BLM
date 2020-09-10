from django.conf.urls import url

from HomeApp import views

urlpatterns = [
    # app主页面
    url(r'^home/', views.home, name='home'),

]
