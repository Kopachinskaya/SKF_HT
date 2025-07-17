from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm
from django.urls import reverse_lazy


class NewsList(ListView):
    ordering = '-creation_date'
    queryset = Post.objects.filter(
         category_type = 'NW'
     )
    template_name = 'news.html'
    context_object_name = 'news'

    #pagination
    paginate_by = 10

    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = NewsFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    

class ArticlesList(ListView):
    ordering = '-creation_date'
    queryset = Post.objects.filter(
        category_type = 'AR'
        )
    template_name = 'articles.html'
    context_object_name = 'articles'

        #pagination
    paginate_by = 10

    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = NewsFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    

class NArticleDetail(DetailView):
    queryset = Post.objects.filter(
         category_type = 'NW'
     )
    # Используем другой шаблон — product.html
    template_name = 'n_article.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'n_article'

class AArticleDetail(DetailView):
    queryset = Post.objects.filter(
         category_type = 'AR'
     )
    # Используем другой шаблон — product.html
    template_name = 'a_article.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'a_article'

class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.category_type = 'NW'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.category_type = 'AR'
        return super().form_valid(form)
    
class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

class ArticlesUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_create.html'

# Представление удаляющее запись.
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')