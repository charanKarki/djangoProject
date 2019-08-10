from django.contrib import admin
from .models import blog,blog_likes,blog_comments
# Register your models here.
admin.site.register(blog)
admin.site.register(blog_likes)
admin.site.register(blog_comments)
