#-*- coding: utf-8 -*-

# author: li yangjin

from django.template import Library

register = Library()

@register.filter
def replaceTags(content):  #这里应该需要继续研究下，有时候需要空格，而不是&nbsp;
    content = content.replace("  ", "&nbsp;&nbsp;")  # 预处理空格
    content = content.replace("\n", "<br/>")  # 预处理换行
    return content

register.filter('replaceTags', replaceTags)