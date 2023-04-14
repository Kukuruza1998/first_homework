import os, pprint

MENU = {
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
  for key, value in MENU.items():
    print(f"{key}. {MENU[key]}")       

def print_all_login(state):
  for key, value in state.items():  
    if value['login'] is not None: 
      print(f"Пользователь: {value['login']}")

def validation_print_choice_2(state, a):
  for key,value in state.items():
    if a!=value['login']:
      clear_terminal()
      print(f"Пользователя c таким логином не существует \n")
      continue
    else:
      clear_terminal()
      print(f"Данные пользователя '{value['login']}':")
      pprint.pprint(value)
      print()
    break 

def validation_change_choice_3(state, a):
  for key,value in state.items():
    if a!=value['login']:
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

def validation_delete_choice_4(state, a):
  for key,value in state.items():   
    if a!=value['login']:
      clear_terminal()
      print(f"Пользователя c таким логином не существует \n")
      continue
    else:
      clear_terminal()
      print(f"Пользователь с логином '{state[key]}' удалён")
      del state[key]
    break

def calculation_bmi(weight, height):
  return round(float(weight)/((float(height)*0.01)**2))      

def main():
  clear_terminal()
  _state={}
  id=0

  while(True):
    print_menu()
    choice = input(f"\n Ваш выбор: ")

    if choice.isdigit() and int(choice) == 1:
      clear_terminal()
      if _state !={}:
        print('Список всех пользователей: ')
        print_all_login(_state)
        print()
          

    elif choice.isdigit() and int(choice) == 2:
      clear_terminal()
      if _state=={}:
        pass
      else:
        while True:
          print_all_login(_state)
          login_to_valid = \
            input('Введите логин пользователя, которого хотите просмотреть:')
          validation_print_choice_2(_state, login_to_valid)
          break
      
      
    elif choice.isdigit() and int(choice) == 3:
      clear_terminal()
      if _state=={}:
        pass
      else:
        while True:
          print_all_login(_state)
          login_to_valid = \
            input('Введите логин пользователя, которого хотите изменить: ') 
          validation_change_choice_3(_state, login_to_valid)
          break   

    elif choice.isdigit() and int(choice) == 4:
      clear_terminal()
      if _state=={}:
        pass
      else:
        while True:
          print_all_login(_state)
          login_to_valid = \
            input('Введите логин пользователя, которого хотите удалить: ')
          validation_delete_choice_4(_state, login_to_valid) 
          break

    elif choice.isdigit() and int(choice) == 5:
      clear_terminal()
      _login = input(f"Введите логин пользователя(not ''): ")
      if not _login =="" \
        or print("Некоректное заполнение логина", end='\n'*2):

        _gender = input(f"Введите пол пользователя(male/female): ")
        if  _gender == 'male' or  _gender == 'female' \
          or print("Некоректное заполнение пола", end='\n'*2):

          _age = input(f"Введите возраст пользователя(1...99): ") 
          if _age.isdigit() and _age !="" and 0<int(_age)<100 \
            or print("Некоректное заполнение возроста", end='\n'*2):

            _height = input(f"Введите рост пользователя(1...250 см): ")
            if  _height.isdigit() and 0<int(_height)<251 \
              and not _height == "" \
                or print("Некоректное заполнение роста", end='\n'*2): 

              _weight = input(f"Введите вес пользователя(1...200 кг): ")
              if  _weight.isdigit() and 0<int(_weight)<201 \
                and not _weight == "" \
                  or print("Некоректное заполнение веса", end='\n'*2):

                _state[id]={
                  'login':_login,
                  'weight':_weight,
                  'height':_height,
                  'gender':_gender,
                  'age':_age,
                  'bmi':(calculation_bmi(_weight,_height)),
                }
            
                id+=1 
                clear_terminal()
                print("Пользователь добавлен в список", end='\n'*2)
                                   
        
    elif choice.isdigit() and int(choice) == 6:
      exit()
    
    else:
      clear_terminal()
      print('Некорректный выбор!',end="\n"*2)


main()