from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    ordering = '-creation_date'
    queryset = Post.objects.filter(
         category_type = 'NW'
     )
    template_name = 'news.html'
    context_object_name = 'news'

class NArticleDetail(DetailView):
    queryset = Post.objects.filter(
         category_type = 'NW'
     )
    # Используем другой шаблон — product.html
    template_name = 'n_article.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'n_article'