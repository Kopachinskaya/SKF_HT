# HW-03 2.9 Команды запускаемые в Shell

```
from news.models import*
```
<ul>
<ol>Создать двух пользователей (с помощью метода User.objects.create_user('username')).</ol>
```
>>> user_1 = User.objects.create_user(username='Петров Петр Петрович')
>>> user_2 = User.objects.create_user(username='Иванов Иван Иванович') 
```
<ol>Создать два объекта модели Author, связанные с пользователями.</ol>
```
>>> author_1= Author.objects.create(author_user=user_1)                 
>>> author_2 = Author.objects.create(author_user=user_2)
```
<ol>Добавить 4 категории в модель Category.</ol>
```
>>> category_1 = Category.objects.create(name = 'Спорт')     
>>> category_2 = Category.objects.create(name = 'Культура') 
>>> category_3= Category.objects.create(name = 'Образование') 
>>> category_4 = Category.objects.create(name = 'Наука') 
```
<ol>Добавить 2 статьи и 1 новость.</ol>
```
>>> article_1 = Post.objects.create(author = author_1, category_type = 'AR', title = 'Первая статья', text = 'Sample text')      
>>> article_2= Post.objects.create(author = author_2, category_type = 'AR', title = 'Вторая статья', text = 'Sample text II')   
>>> news_1= Post.objects.create(author = author_1, category_type = 'NW', title = 'Новость!', text = 'Sample news text')
```
</ul>
