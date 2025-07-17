from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList,ArticlesList,ArticleCreate, NArticleDetail, AArticleDetail,NewsCreate, NewsUpdate, ArticlesUpdate, PostDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name = 'news'), 
   path('<int:pk>', NArticleDetail.as_view(), name = 'n_article'),
   path('create/', NewsCreate.as_view(), name = 'news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name = 'news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name = 'news_delete'),
   path('articles/', ArticlesList.as_view(), name = 'articles'), 
   path('articles/<int:pk>', AArticleDetail.as_view(), name = 'a_article'),
   path('articles/create/', ArticleCreate.as_view(), name = 'article_create'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name = 'articles_update'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete'),
]