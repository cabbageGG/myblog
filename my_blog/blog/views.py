from django.shortcuts import render
from django.views.generic.base import View
from blog import models
from datetime import datetime
# Create your views here.

def index(request):
    blogs = models.Blog.objects.all()
    return render(request, "blog/index.html", {"blogs": blogs})

def blogs(request):
    blogs = models.Blog.objects.all()
    return render(request, "blog/blogs.html", {"blogs": blogs})

def show_blog(request, blog_id):
    blog = models.Blog.objects.get(pk=blog_id)
    return render(request, "blog/blog.html", {"blog": blog})

def edit_blog(request, blog_id):
    if str(blog_id) == '0':
        return render(request, "blog/blog_edit.html")
    blog = models.Blog.objects.get(pk=blog_id)
    return render(request, "blog/blog_edit.html", {"blog": blog})

def save_blog(request):
    title = request.POST.get("title", "TITLE")
    content = request.POST.get("content", "")
    blog_id = request.POST.get("blog_id", "0")
    if blog_id == '0':
        models.Blog.objects.create(titile=title, content=content, create_time=datetime.now())
        blogs = models.Blog.objects.all()
        return render(request, "blog/blogs.html", {"blogs": blogs})
    blog = models.Blog.objects.get(pk=blog_id)
    blog.titile = title
    blog.content = content
    blog.create_time = datetime.now()
    blog.save()
    return render(request, "blog/blog.html", {"blog": blog})

def delete_blog(request, blog_id):
    pass


