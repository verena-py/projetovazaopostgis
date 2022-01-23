
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.paginainicial, name='paginainicial'),
    path('projeto/', views.projeto, name='projeto'),
    path('dados/', views.dados, name='dados'),

]