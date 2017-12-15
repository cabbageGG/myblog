#-*- coding: utf-8 -*-

# author: li yangjin

from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.blogs, name="index"),
    url(r'^page/(?P<blog_id>\d+)/$', views.show_blog, name="show_blog"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^register/$', views.register, name="register"),
    url(r'^signout/$', views.signout, name="signout"),
    url(r'^comment/$', views.comment, name="comment"),
    url(r'^uploadImg/$', views.uploadImg, name="uploadImg"),
    url(r'^comment_reply/$', views.comment_reply, name="comment_reply"),
]