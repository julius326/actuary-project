from django.urls import path
from . import views

urlpatterns = [
    path('', views.hom, name='hom'),
    path('index', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
    path('averages/', views.averages, name='averages'),


]
