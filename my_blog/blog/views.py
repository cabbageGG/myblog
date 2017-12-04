# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from blog import models
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    blogs = models.Blog.objects.all()
    return render(request, "blog/index.html", {"blogs": blogs})

def blogs(request):
    blogs = models.Blog.objects.all()
    return render(request, "blog/blogs.html", {"blogs": blogs})

def show_blog(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    return render(request, "blog/blog.html", {"blog": blog})

def edit_blog(request, blog_id):
    if str(blog_id) == '0':
        return render(request, "blog/blog_edit.html")
    blog = models.Blog.objects.get(id=blog_id)
    return render(request, "blog/blog_edit.html", {"blog": blog})

def save_blog(request):
    title = request.POST.get("title", "TITLE")
    summary = request.POST.get("summary", "")
    content = request.POST.get("content", "")
    blog_id = request.POST.get("blog_id", "0")
    if blog_id == '0':
        models.Blog.objects.create(title=title, summary=summary, content=content, create_time=datetime.now())
        blogs = models.Blog.objects.all()
        return render(request, "blog/blogs.html", {"blogs": blogs})
    blog = models.Blog.objects.get(id=blog_id)
    blog.title = title
    blog.summary = summary
    blog.content = content
    blog.create_time = datetime.now()
    blog.save()
    return render(request, "blog/blog.html", {"blog": blog})

def delete_blog(request, blog_id):
    models.Blog.objects.filter(id=blog_id).delete()
    blogs = models.Blog.objects.all()
    return render(request, "blog/blogs.html", {"blogs": blogs})

def comment_blog(request, blog_id):
    pass

def signin(request):
    return render(request, "blog/signin.html")

def register(request):
    return render(request, "blog/register.html")

def signin_action(request):
    account = request.POST.get("account", "")
    password = request.POST.get("password", "")
    user = models.User.objects.filter(account=account,passwd=password)
    if user:
        blogs = models.Blog.objects.all()
        return render(request, "blog/index.html", {"blogs": blogs})
    return render(request, "blog/signin.html")

def register_action(request):
    name = request.POST.get("name", "")
    account = request.POST.get("account", "")
    password1 = request.POST.get("password1", "")
    password2 = request.POST.get("password2", "")
    if password1 != password2 or password1 == "" or password2 == "":
        #return render(request, "blog/register.html")
        return HttpResponse("密码错误")
    if account:
        user = models.User.objects.filter(account=account)
        if user:
            #return render(request, "blog/register.html")
            return HttpResponse("用户已存在")
        else:
            models.User.objects.create(name=name, account=account, passwd=password1)
            blogs = models.Blog.objects.all()
            return render(request, "blog/index.html", {"blogs": blogs})
    else:
        #return render(request, "blog/register.html")
        return HttpResponse("账户为空")

