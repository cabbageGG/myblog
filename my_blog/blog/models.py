# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=32, default="Title")
    content = models.TextField()
    summary = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    view_times = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title
    
    class Meta:
        db_table = 'blog'

class User(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='img', null=True)
    account = models.CharField(max_length=32, null=True)
    passwd = models.CharField(max_length=32, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'user'

class Comments(models.Model):
    username = models.CharField(max_length=32, default="passinger")
    userimage = models.ImageField(upload_to='img', null=True)
    blog_id = models.IntegerField() #表示他是博客blog_id的评论
    parent_id = models.IntegerField(default=0) #记录根评论的id。parent_id可以定位到该评论放在那里。
    comment_id = models.IntegerField(default=0) #默认为0，表示他是一条评论; 当有comment_id值时，表示他是评论comment_id的留言,用于指明回复的对象。
    comment_username = models.CharField(max_length=32, null=True)  # 评论回复对象的用户名
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.username
    
    class Meta:
        db_table = 'comments'




