from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^order/', views.order, name='order')
]
