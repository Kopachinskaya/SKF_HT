from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Category

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
   
   # по категории (связующая таблица PostCategory и category_through)
    category = ModelChoiceFilter(
       field_name = 'postcategory__category_through',
       queryset = Category.objects.all(),
       label='Category',
       empty_label = 'Не имеет значения')

    # Фильтер по дате
    added_after = DateTimeFilter(
        field_name='creation_date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
   )

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['contains'],
       }