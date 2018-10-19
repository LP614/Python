"""new python"""
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^info/(?P<id>\d+)/', views.info, name='info'),
]