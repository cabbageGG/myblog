#coding:utf8
from rest_framework import serializers
from blog.models import Blog, Comments

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title','content','summary','create_time','update_time','view_times')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('username','userimage','blog_id','parent_id','comment_id','comment_username','content','create_time')

    def validate(self, data):
        '''
           validate blog_id 
           TODO: validate_blog_id 与 validate 的区别？
        '''
        blog = Blog.objects.filter(id=data['blog_id'])
        print(blog)
        if not blog:
            raise serializers.ValidationError("wrong blog_id, blog not exist")
        return data
    