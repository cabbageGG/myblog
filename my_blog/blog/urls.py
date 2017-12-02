#-*- coding: utf-8 -*-

# author: li yangjin

from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.blogs, name="index"),
    url(r'^page/(?P<blog_id>\d+)/$', views.show_blog, name="show_blog"),
    url(r'^edit/(?P<blog_id>\d+)/$', views.edit_blog, name="edit_blog"),
    url(r'^save/$', views.save_blog, name="save_blog"),
    url(r'^delete/(?P<blog_id>\d+)/$', views.delete_blog, name="delete_blog"),
]