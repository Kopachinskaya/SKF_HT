# HW-03 2.9 Команды запускаемые в Shell

```
from news.models import*
```
### 1.Создать двух пользователей (с помощью метода User.objects.create_user('username')).
  
```
>>> user_1 = User.objects.create_user(username='Петров Петр Петрович')
>>> user_2 = User.objects.create_user(username='Иванов Иван Иванович') 
```

### 2.Создать два объекта модели Author, связанные с пользователями.

```
>>> author_1= Author.objects.create(author_user=user_1)                 
>>> author_2 = Author.objects.create(author_user=user_2)
```

### 3.Добавить 4 категории в модель Category.

```
>>> category_1 = Category.objects.create(name = 'Спорт')     
>>> category_2 = Category.objects.create(name = 'Культура') 
>>> category_3= Category.objects.create(name = 'Образование') 
>>> category_4 = Category.objects.create(name = 'Наука') 
```

### 4.Добавить 2 статьи и 1 новость.

```
>>> article_1 = Post.objects.create(author = author_1, category_type = 'AR', title = 'Первая статья', text = 'Sample text')      
>>> article_2= Post.objects.create(author = author_2, category_type = 'AR', title = 'Вторая статья', text = 'Sample text II')   
>>> news_1= Post.objects.create(author = author_1, category_type = 'NW', title = 'Новость!', text = 'Sample news text')
```

### 5.Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

```
>>> post_cat_1= Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))                                            
>>> post_cat_2= Post.objects.get(id=2).post_category.add(Category.objects.get(id=1))   
>>> post_cat_2_1= Post.objects.get(id=2).post_category.add(Category.objects.get(id=3))      
>>> post_cat_3= Post.objects.get(id=3).post_category.add(Category.objects.get(id=4))
```

### 6.Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

```
>>> comm_1 = Comment.objects.create(comment_post =Post.objects.get(id=1),comment_user = Author.objects.get(id=1).author_user, text = 'Positive comment text')  
>>> comm_2 = Comment.objects.create(comment_post =Post.objects.get(id=2),comment_user = Author.objects.get(id=2).author_user, text = 'Positive comment text II') 
>>> comm_3= Comment.objects.create(comment_post =Post.objects.get(id=2),comment_user = Author.objects.get(id=2).author_user, text = 'Negative comment text')     
>>> comm_4= Comment.objects.create(comment_post =Post.objects.get(id=3),comment_user = Author.objects.get(id=1).author_user, text = 'Positive comment text III')
```

### 7.Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
#### Пример:

```
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=2).dislike()
>>> Post.objects.get(id=3).dislike()
>>> Post.objects.get(id=2).like()
```

### 8.Обновить рейтинги пользователей.

```
>>> a_raiting_1 = Author.objects.get(id=1) 
>>> a_raiting_1.update_rating()
>>> a_raiting_1.rating_author
9
>>> a_raiting_2 = Author.objects.get(id=2)  
>>> a_raiting_2.update_rating()            
>>> a_raiting_2.rating_author  
7
```

### 9.Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

```
>>> best_user = Author.objects.order_by('-rating_author')[:1]
>>> best_user.values('author_user__username','rating_author') 
```

### 10.Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

```
>>> best_post = Post.objects.order_by('-rating')[:1]
>>> best_post.values('creation_date','author__author_user__username','rating','title')
>>> Post.objects.order_by('-rating')[0].preview() 

```

### 11.Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

```
>>> id_best = best_post.values('id')[0]
>>> Comment.objects.filter(comment_post_id=id_best.get('id')).values('creation_date','comment_user__username','rating','text')

```
