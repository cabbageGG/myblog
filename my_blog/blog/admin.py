from django.contrib import admin
from blog.models import Blog, User

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')
    search_fields = ('title', 'create_time')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'account')
    search_fields = ('name', 'account')

admin.site.register(Blog, BlogAdmin)
admin.site.register(User, UserAdmin)