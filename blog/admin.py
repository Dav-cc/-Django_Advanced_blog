from django.contrib import admin
from blog.models import Category , Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status']
    list_filter = ['author', 'title']






admin.site.register(Category)
admin.site.register(Post)
