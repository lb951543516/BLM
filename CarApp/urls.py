from django.conf.urls import url

from CarApp import views

urlpatterns = [
    url(r'^car/', views.car, name='car')
]
