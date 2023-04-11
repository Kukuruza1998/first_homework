import os, pprint

menu = {
     1:'Вывести список пользователей',
     2:'Посмотреть информацию о пользователе(рост, вес, ИМТ)',
     3:'Изменить данные о пользователе',
     4:'Удалить выбранного пользователя',
     5:'Добавить пользователя',
     6:'Выход',
 }

def print_menu():
     for key in menu.keys():
        print(f"{key}. {menu[key]}")

def show_history(state):      
      return state      

def choice_2():
      print('Посмотреть информацию о пользователе(рост, вес, ИМТ)')

def choice_3():
      print('Изменить данные о пользователе')      

def choice_4():
      print('Удалить выбранного пользователя')      

def calculator_bmi(weight, height):
      return round(float(weight)/((float(height)*0.01)**2))      

os.system('CLS')
_state={}
id=0
while(True):
  _weight,_height,_gender,_age=70,190,"male",24
  print_menu()
  choice = int(input(f"\n Ваш выбор: "))
  if choice == 1:
      os.system('CLS')
      pprint.pprint(show_history(_state))
      print()
  elif choice == 2:
      choice_2()
  elif choice == 3:
      choice_3()
  elif choice == 4:
      choice_4()
  elif choice == 5:
    _state[id]={
        'weight':_weight,
        'height':_height,
        'gender':_gender,
        'age':_age,
        'bmi':(calculator_bmi(_weight,_height))
        }
    id+=1
    os.system('CLS')
  elif choice == 6:
      break
  else:
      os.system('CLS')
      print('Некорректный выбор!',end="\n"*2)


