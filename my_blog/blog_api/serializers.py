from rest_framework import serializers
from blog.models import Blog, Comments

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

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
    