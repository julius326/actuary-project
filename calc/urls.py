from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('hom/', views.hom, name='hom'),
    path('pc', views.pc, name='pc'),
    path('calculate/', views.calculate, name='calculate'),
    path('moct/', views.moct, name='moct'),
    path('SMA3101/', views.SMA3101, name='SMA3101'),
    path('ITAS/', views.ITAS, name='ITAS'),
    path('mod/', views.mod, name='mod'),
    path('probability/', views.probability, name='probability'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login, name='login'),
    path('logout_view/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('interests/', views.interests, name='interests'),
    path('amountsi/', views.amountsi, name='amountsi'),

]
