# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)
    summary = models.TextField(null=True)
    create_time = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=32)
    head_img = models.ImageField(upload_to='head_img', null=True)
    account = models.CharField(max_length=32, null=True)
    passwd = models.CharField(max_length=32, null=True)
    def __unicode__(self):
        return self.name

class Comments(models.Model):
    username = models.CharField(max_length=32, default="passinger")
    userimg = models.ImageField(upload_to='head_img', null=True)
    blog_id = models.IntegerField() #表示他是博客blog_id的评论
    comment_id = models.IntegerField(default=0) #默认为0，表示他是一条评论; 当有comment_id值时，表示他是评论comment_id的留言
    content = models.TextField()
    create_time = models.DateTimeField()
    def __unicode__(self):
        return self.username




