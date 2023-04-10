import os
menu = {
     1:'Вывести список пользователей',
     2:'Посмотреть информацию о пользователе(рост, вес, ИМТ)',
     3:'Изменить данные о пользователе',
     4:'Удалить выбранного пользователя',
     5:'Добавить пользователя',
     6:'Выход',
 }
dict_person = {}
def print_menu():
     for key in menu.keys():
         print(f"{key}. {menu[key]}")

def choice_1():
      os.system('CLS')
      print('Вывести список пользователей')      

def choice_2():
      os.system('CLS')
      print('Посмотреть информацию о пользователе(рост, вес, ИМТ)')

def choice_3():
      os.system('CLS')
      print('Изменить данные о пользователе')      

def choice_4():
      os.system('CLS')
      print('Удалить выбранного пользователя')      

def choice_5():
      os.system('CLS')
      print('Добавить пользователя')      

os.system('CLS')
while(True):
  print_menu()
  choice = int(input(f"\n Ваш выбор: "))
  if choice == 1:
     choice_1()
  elif choice == 2:
      choice_2()
  elif choice == 3:
      choice_3()
  elif choice == 4:
      choice_4()
  elif choice == 5:
      choice_5()
  elif choice == 6:
      break
  else:
      os.system('CLS')
      print('Некорректный выбор!',end="\n"*2)


