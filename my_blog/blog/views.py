from django.shortcuts import render
from django.views.generic.base import View
from blog import models
from datetime import datetime
# Create your views here.

class IndexView(View):
    def get(self, request):
        # time = datetime.now()
        # models.Blog.objects.create(titile="my second blog",content="good good study, day day up !",create_time=time)
        blogs = models.Blog.objects.all()
        return render(request, "index.html", {"blogs":blogs})

class BlogView(View):
    def get(self, request, blog_id):
        blog = models.Blog.objects.get(pk=blog_id)
        return render(request, "blog.html",{"blog":blog})

class BlogEditView(View):
    def get(self, request, blog_id):
        if str(blog_id) == '0':
            return render(request, "blog_edit.html")
        blog = models.Blog.objects.get(pk=blog_id)
        return render(request, "blog_edit.html",{"blog":blog})

class BlogSaveView(View):
    def get(self, request):
        title = request.POST.get("title","TITLE")
        content = request.POST.get("content","")
        blog_id = request.POST.get("blog_id","0")
        if blog_id == '0':
            models.Blog.objects.create(titile=title, content=content,create_time=datetime.now())
            blogs = models.Blog.objects.all()
            return render(request, "index.html", {"blogs": blogs})
        blog = models.Blog.objects.get(pk=blog_id)
        blog.titile = title
        blog.content = content
        blog.create_time = datetime.now()
        blog.save()
        return render(request, "blog.html", {"blog": blog})


