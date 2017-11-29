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

