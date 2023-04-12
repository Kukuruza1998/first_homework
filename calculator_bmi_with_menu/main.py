import os, pprint

menu = {
     1:'Вывести список пользователей',
     2:'Посмотреть информацию о пользователе(рост, вес, ИМТ)',
     3:'Изменить данные о пользователе',
     4:'Удалить выбранного пользователя',
     5:'Добавить пользователя',
     6:'Выход',
 }

def clear_terminal():
    return os.system('CLS')

def print_menu():
     for key in menu.keys():
        print(f"{key}. {menu[key]}")

def show_history(state):      
      return state      

def choice_3():
      print('Изменить данные о пользователе')      

def choice_4():
      print('Удалить выбранного пользователя')      

def calculator_bmi(weight, height):
      return round(float(weight)/((float(height)*0.01)**2))      

clear_terminal()
_state={}
id=0


while(True):
  print_menu()
  choice = input(f"\n Ваш выбор: ")

  if choice.isdigit() and int(choice) == 1:
      clear_terminal()
      if _state !={}:
        for value in _state.values():
          pprint.pprint(f"Пользователь: {value['login']}")   
      else:
        print()
      

  elif choice.isdigit() and int(choice) == 2:
    clear_terminal()
    if _state=={}:
        pass
    else:
      for key,value in _state.items():
        pprint.pprint(value['login'])
      
      while True:
        login_to_valid = input('Введите логин пользователя, которого хотите просмотреть:')
        for key,value in _state.items():
          
          if login_to_valid!=value['login']:
            clear_terminal()
            print(f"Пользователя c таким логином не существует \n")
            continue
          else:
            clear_terminal()
            pprint.pprint(value)
            print()
          break  
        
        break
    
  elif choice.isdigit() and int(choice) == 3:
    clear_terminal()
    if _state=={}:
        pass
    else:
      for key,value in _state.items():
        pprint.pprint(value['login'])
      
      while True:
        login_to_valid = input('Введите логин пользователя, которого хотите изменить: ')
        for key,value in _state.items():
          
          if login_to_valid!=value['login']:
            clear_terminal()
            print(f"Пользователя c таким логином не существует \n")
            continue
          else:
            clear_terminal()
            pprint.pprint(value)
            change_parameter = \
              input('Введите название ключа которое хотите изменить: ')
            for x in value:
              if change_parameter==x:
                 value[x]=input('Введите значение: ')
            clear_terminal()
          break  
        
        break

  elif choice.isdigit() and int(choice) == 4:
    clear_terminal()
    if _state=={}:
        pass
    else:
      for key,value in _state.items():
        pprint.pprint(value['login'])
      
      while True:
        login_to_valid = input('Введите логин пользователя, которого хотите удалить:')
        for key,value in _state.items():
          
          if login_to_valid!=value['login']:
            clear_terminal()
            print(f"Пользователя c таким логином не существует \n")
            continue
          else:
            clear_terminal()
            del _state[key]
            print()
          break  
        
        break

  elif choice.isdigit() and int(choice) == 5:
    clear_terminal()
    _login = input(f"Введите логин пользователя: ")
    _weight = input(f"Введите вес пользователя(кг): ")
    _height = input(f"Введите рост пользователя(см): ")
    _gender = input(f"Введите пол пользователя: ")
    _age = input(f"Введите возраст пользователя: ")
    _state[id]={
    'login':_login,
    'weight':_weight,
    'height':_height,
    'gender':_gender,
    'age':_age,
    'bmi':(calculator_bmi(_weight,_height)),
    }
    id+=1  
    clear_terminal()

  elif choice.isdigit() and int(choice) == 6:
      exit()
  
  else:
      clear_terminal()
      print('Некорректный выбор!',end="\n"*2)


#сделать проверки на ввод, постараться сделать функции и декоратор. \
# условно фор в функ а в декораторе выводить значеня красивыми или проверять key value