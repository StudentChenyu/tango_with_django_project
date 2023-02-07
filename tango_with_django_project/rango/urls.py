# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:56:54 2023

@author: Aluneth
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
         views.show_category,
         name='show_category'),
    ]
