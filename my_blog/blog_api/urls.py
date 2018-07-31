#-*- coding: utf-8 -*-

# author: li yangjin

from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.BlogView.as_view({"get":"list","post":"create"})),
    url(r'^count/$',views.BlogView.as_view({"get":"count"})),
    url(r'^(?P<blog_id>[0-9]+)/$',views.BlogView.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
    url(r'^(?P<blog_id>[0-9]+)/comment/$',views.CommentView.as_view({"get":"list","post":"create"})),
    url(r'^(?P<blog_id>[0-9]+)/comment/count/$',views.CommentView.as_view({"get":"count"})),
    url(r'^(?P<blog_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/$',views.CommentView.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
]