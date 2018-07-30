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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return NormalResponse(result=BlogSerializer(serializer.instance).data)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return NormalResponse(result=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return NormalResponse(result=serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return NormalResponse(result=BlogSerializer(serializer.instance).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return NormalResponse(result={})
    

class CommentView(viewsets.ModelViewSet):
    lookup_url_kwarg = ('comment_id')
    lookup_field = ('id')
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()