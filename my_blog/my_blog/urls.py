"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import blog.views as view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index, name="index"),
    url(r'^blog/$',view.blogs, name="blogs"),
    url(r'^blog/(?P<blog_id>\d+)/$', view.show_blog, name="show_blog"),
    url(r'^blog/blog_edit/(?P<blog_id>\d+)/$', view.edit_blog, name="edit_blog"),
    url(r'^blog/save/$', view.save_blog, name="save_blog"),

]
