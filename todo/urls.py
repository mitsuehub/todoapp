# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='todo'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('done/<int:num>', views.done, name='done'),
    ]
