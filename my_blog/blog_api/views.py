# -*- coding: utf-8 -*-
from rest_framework import viewsets

from blog.models import Blog, Comments
from blog_api.serializers import BlogSerializer, CommentSerializer

from utils.response import NormalResponse

class BlogView(viewsets.ModelViewSet):
    lookup_url_kwarg = ('blog_id')
    lookup_field = ('id')
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def count(self, request, *args, **kwargs):
        count = len(self.get_queryset())
        return NormalResponse({"count":count})

class CommentView(viewsets.ModelViewSet):
    lookup_url_kwarg = ('comment_id')
    lookup_field = ('id')
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()