#-*- coding: utf-8 -*-

# author: li yangjin

from django.template import Library

register = Library()

@register.filter
def replaceTags(content):
    content = content.replace("<", "&lt;")  # 预处理换行
    content = content.replace(">", "&gt;")  # 预处理换行
    content = content.replace(" ", "&nbsp;")  # 预处理空格
    content = content.replace("\n", "<br/>")  # 预处理换行
    return content

register.filter('replaceTags', replaceTags)