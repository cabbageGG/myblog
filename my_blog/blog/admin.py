from django.contrib import admin
from blog.models import Blog, User, Comments

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')
    search_fields = ('title', 'create_time')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'account')
    search_fields = ('name', 'account')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'blog_id', 'comment_id','create_time')
    search_fields = ('username', 'blog_id', 'comment_id','create_time')

admin.site.register(Blog, BlogAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comments, CommentsAdmin)