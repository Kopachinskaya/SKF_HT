from django import template


register = template.Library()

POSSIBLE_CURSES = [
   "редиска",
   "порей",
   "капуста"
]

def replace(word):

    """Проверяет, есть ли слово в списке ругательств"""

    if word.lower() in POSSIBLE_CURSES:
        #Заменяет все буквы, кроме начальной на *
        repl = ''.join([word[0]]+[l.replace(l, "*") for l in word[1:]])
        return repl
    else:
        return word

@register.filter()
def censor(value):
    if type(value)==str:
        #Перезаписывает слово в value если оно ругательное
        value = ' '.join([replace(word) for word in value.split()])
        return f'{value}'
    else:
        return f'{value}'