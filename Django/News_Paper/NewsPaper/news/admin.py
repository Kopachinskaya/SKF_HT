from django.contrib import admin
from .models import Author, Post, Category, PostCategory, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Post)