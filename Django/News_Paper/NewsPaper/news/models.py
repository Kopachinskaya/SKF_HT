from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum



# Create your models here.


class Author(models.Model):

    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author =  models.SmallIntegerField(default=0)

    def __str__(self):
        return self.author_user.username


    def update_rating(self):

        post_rat = self.post_set.aggregate(post_rating = Sum('rating'))
        p_rat = 0
        p_rat += post_rat.get('post_rating')

        comment_rat = self.author_user.comment_set.aggregate(comment_rating = Sum('rating'))
        c_rat = 0
        c_rat += comment_rat.get('comment_rating')

        self.rating_author = p_rat*3 + c_rat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    news = 'NW'
    article = 'AR'

    CATHEGORY_CHOICES = (
        (news, 'Новость'),
        (article, 'Статья')
    )
    category_type = models.CharField(max_length=2, choices=CATHEGORY_CHOICES, default=article)
    creation_date = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()
    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return '{}...'.format(self.text[:125])
    
    def __str__(self):
        return f'Новость от {self.creation_date}: {self.title}  {self.text}'
    
    def get_absolute_url(self):
        if self.category_type == 'NW':
            return reverse('n_article', args=[str(self.id)])
        if self.category_type == 'AR':
            return reverse('a_article', args=[str(self.id)])
    

class PostCategory(models.Model):

    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)

    


class Comment(models.Model):

    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()