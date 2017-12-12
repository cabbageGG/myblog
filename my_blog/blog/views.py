# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog import models
from datetime import datetime
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    userinfo = ""
    account = request.COOKIES.get("account","")
    if account:
        userinfo = models.User.objects.filter(account=account)[0]
    page = int(request.GET.get("p", "1"))
    first = (page - 1)*10
    end = first + 10
    blogs = models.Blog.objects.all()
    total_nums = len(blogs)
    if (total_nums % 10) > 0:
        page_nums = int(total_nums/10) + 1
    else:
        page_nums = int(total_nums/10)

    page_nums = range(0, page_nums)
    blogs = blogs[first:end]
    page = page - 1

    return render(request, "blog/index.html", {"blogs": blogs, "page":page, "page_nums":page_nums, "userinfo":userinfo})

def blogs(request):
    userinfo = ""
    account = request.COOKIES.get("account","")
    if account:
        userinfo = models.User.objects.filter(account=account)[0]
    page = int(request.GET.get("p", "1"))
    first = (page - 1)*10
    end = first + 10
    blogs = models.Blog.objects.all()
    total_nums = len(blogs)
    if (total_nums % 10) > 0:
        page_nums = int(total_nums/10) + 1
    else:
        page_nums = int(total_nums/10)

    page_nums = range(0, page_nums)
    blogs = blogs[first:end]
    page = page - 1

    return render(request, "blog/blogs.html", {"blogs": blogs, "page":page, "page_nums":page_nums, "userinfo":userinfo})

def show_blog(request, blog_id):
    userinfo = ""
    account = request.COOKIES.get("account","")
    if account:
        userinfo = models.User.objects.filter(account=account)[0]
    blog = models.Blog.objects.get(id=blog_id)
    comments = models.Comments.objects.filter(blog_id=blog_id, comment_id=0)
    return render(request, "blog/blog.html", {"blog": blog, "comments":comments, "userinfo":userinfo})

def comment_blog(request, blog_id):
    user_name = request.POST.get("user_name", "游客")
    account = request.COOKIES.get("account","")
    if account:
        user = models.User.objects.filter(account=account)
        user_name = user[0].name
    blog_id = request.POST.get("blog_id", "1")
    comment_id = request.POST.get("comment_id", "0")
    content = request.POST.get("content", "")
    models.Comments.objects.create(username=user_name, blog_id=blog_id, comment_id=comment_id, content=content, create_time=datetime.now())
    return HttpResponseRedirect("/blog/page/%s" % blog_id)

def signin(request):
    return render(request, "blog/signin.html")

def register(request):
    return render(request, "blog/register.html")

def signout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie(key="account")
    return response

def signin_action(request):
    account = request.POST.get("account", "")
    password = request.POST.get("password", "")
    user = models.User.objects.filter(account=account,passwd=password)
    if user:
        response = HttpResponseRedirect("/blog")
        response.set_cookie(key='account', value=account, expires=3600)
        return response
    return render(request, "blog/signin.html", {"msg":"登录失败"})

def register_action(request):
    name = request.POST.get("name", "")
    account = request.POST.get("account", "")
    password1 = request.POST.get("password1", "")
    password2 = request.POST.get("password2", "")
    if  password1 == "" or password2 == "":
        return render(request, "blog/register.html",{"msg":"密码不能为空"})
    if password1 != password2:
        return render(request, "blog/register.html", {"msg": "两次密码不相同"})
    if account:
        user = models.User.objects.filter(account=account)
        if user:
            return render(request, "blog/register.html", {"msg":"用户已存在"})
        else:
            models.User.objects.create(name=name, account=account, passwd=password1)
            return HttpResponseRedirect('/blog')
    else:
        return render(request, "blog/register.html", {"msg":"账户为空"})

