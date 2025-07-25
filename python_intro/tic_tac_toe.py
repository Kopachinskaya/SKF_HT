
# Игра написана только с использованием встроенных функций python и материала курса 
# Победить в игре можно при выполнении одного из трех условий: собрать ряд, собрать диагональ, собрать столбец


#Функция для отслеживания выполнения первого условия, принимает координату хода по горизонтали, текущее состояние поля и переданное пользователем значение
def check_rows_first(i, table, value):

  '''Функция проверяет заполнение ряда одинаковыми значениями.''' 
  '''Если после хода игрока длина множества равна единице и совпадает с введенным игроком символом - проверка пройдена'''

  if len(set(table[i][1:]))==1:
    if value in set(table[i]):
      return True

#Функция для отслеживания выполнения второго условия, принимает текущее состояние поля и переданное пользователем значение
def check_diag_second(table, value):

  '''Функция проверяет заполнение одной из двух горизонталей одинаковыми значениями.'''
  '''Создаются два множества для отслеживания горизонталей'''
  '''Если в ходе игры длина множества становится равной еденице и значение совпадает с вводом игрока - проверка пройдена'''


  diag_1 = list(set([table[1][1], table[2][2], table[3][3]]))
  diag_2 = list(set([table[1][3], table[2][2], table[3][1]]))

  if value in diag_1 and len(diag_1) ==1 or value in diag_2 and len(diag_2) == 1:
    return True

#Функция для отслеживания выполнения третьего условия, принимает текущее состояние поля и переданное пользователем значение
def check_columns_fird(table, value):

  '''Функция проверяет заполнение столбца одинаковыми значениями.'''
  '''Создаются списки значений в столбцах поля.'''
  '''Если в ходе игры длина множества столбца становится равной еденице и значение совпадает с вводом игрока - проверка пройдена'''

  columns= []
  for i in range(len(table)):
      column = [table[j][i] for j in range(len(table[i]))]
      columns.append(column)

  for column in columns:
    if len(set(column[1:])) == 1:
      if value in set(column[1:]):
        return True

#Тело игры
def the_game():
    #Отрисовываем таблицу
    table = [
        [' ', 1,2,3],
        [1, '-', '-', '-'],
        [2, '-', '-', '-'],
        [3, '-', '-', '-'],
        ]
    for row in table:
      for elem in row:
        print(elem, end = " ")
      print()
  #Цикл игры
    while True:

      # play_table = table.copy()
      turn = input("Введите через пробел координаты и значения: Х или 0 ")

      #Проверяем, не хочет ли игрок завершить игру мануально
      if turn.lower() == 'stop':
        print('Игра завершена')
        break
    
      else:
        #Проверяем соответствует ли ввод требуемому формату
        if ' ' not in turn:
          print("Пожалуйста, укажите значения через пробел")
          continue

        else:
          #Если формат верен, начинаем/продолжаем игру
          try:
            turn = turn.split(' ')
            #достаем координату по горизонтали
            i = int(turn[0])
            #достаем координату по вертикали
            j = int(turn[1])
            #достаем и записивыем значение
            value = str(turn[2]).upper()
            table[i][j] = value

          #Отрисовываем таблицу с полученным значением после хода
            for row in table:
              for elem in row:
                print(elem, end = " ")
              print()  

          # Проверка выполнения победных условий
            if check_rows_first(i, table, value) is True:
              print('Выиграл {} собрав ряд'.format(value))
              break
            if check_diag_second(table, value) is True:
              print('Выиграл {} собрав диагональ'.format(value))
              break
            if check_columns_fird(table, value) is True:
              print('Выиграл {} собрав столбец'.format(value))
              break
            else:
              continue

          #Проверка других возможных ошибок ввода
          except IndexError:
            print('Значения введены неверно, попробуйте еще раз')
            continue

def main():
  return the_game()

if __name__ == '__main__':
    main()