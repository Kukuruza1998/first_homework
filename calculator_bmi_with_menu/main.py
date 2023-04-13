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
      del state[key]
      print()
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
          print_all_login(_state)
          print()
          

    elif choice.isdigit() and int(choice) == 2:
      clear_terminal()
      if _state=={}:
        pass
      else:
        while True:
          print_all_login(_state)
          login_to_valid = input('Введите логин пользователя, которого хотите просмотреть:')
          validation_print_choice_2(_state, login_to_valid)
          break
      
      
    elif choice.isdigit() and int(choice) == 3:
      clear_terminal()
      if _state=={}:
        pass
      else:
        while True:
          print_all_login(_state)
          login_to_valid = input('Введите логин пользователя, которого хотите изменить: ') 
          validation_change_choice_3(_state, login_to_valid)
          break   

    elif choice.isdigit() and int(choice) == 4:
      clear_terminal()
      if _state=={}:
        pass
      else:
        while True:
          print_all_login(_state)
          login_to_valid = input('Введите логин пользователя, которого хотите изменить: ')
          validation_delete_choice_4(_state, login_to_valid) 
          break

    elif choice.isdigit() and int(choice) == 5:
      clear_terminal()
      
      # while True:
      #   _login = input(f"Введите логин пользователя: ")
      #   if _login =="":
      #     print("Некорректный ввод логина!")
      #   else:
      #     _gender = input(f"Введите пол пользователя: ")
      #     if _gender.lower != "male" and _gender.lower != "female":
      #       print("Некорректный ввод пола!")
      #     else:
      #       _age = input(f"Введите возраст пользователя: ") 
      #       if (not _age.isdigit()) and not _age.isdigit()>100:
      #         print("Некорректный ввод возроста!")
      #       else:
      #         _height = input(f"Введите рост пользователя(см): ")
      #         if not _height.isdigit() or _height == "":
      #           print("Некорректный ввод роста!")
      #         else:
      #             _weight = input(f"Введите вес пользователя(кг): ")
      #             if not _weight.isdigit() or _weight == "":
      #               print("Некорректный ввод веса!")
      #             else:
      #               _state[id]={
      #               'login':_login,
      #               'weight':_weight,
      #               'height':_height,
      #               'gender':_gender,
      #               'age':_age,
      #               'bmi':(calculation_bmi(_weight,_height)),
      #               }
      #               id+=1  
      #               clear_terminal() 
      #               break
      _login = input(f"Введите логин пользователя: ")
      if not _login =="":
        _gender = input(f"Введите пол пользователя: ")
        if  _gender == 'male' or  _gender == 'female':
          _age = input(f"Введите возраст пользователя: ") 
          if _age.isdigit() and _age !="" and int(_age)<100:
            _height = input(f"Введите рост пользователя(см): ")
            if  _height.isdigit() and not _height == "": 
              _weight = input(f"Введите вес пользователя(кг): ")
              if  _weight.isdigit() and not _weight == "":  
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
                print("Некоректное заполнение данных", end='\n'*2)
              else:
                clear_terminal() 
                print("Некоректное заполнение данных", end='\n'*2)
            else:
              clear_terminal()
              print("Некоректное заполнение данных", end='\n'*2)
          else:
            clear_terminal()
            print("Некоректное заполнение данных", end='\n'*2)
        else:
          clear_terminal()
          print("Некоректное заполнение данных", end='\n'*2)
      else:
         clear_terminal()
         print("Некоректное заполнение данных", end='\n'*2)                     
        
    elif choice.isdigit() and int(choice) == 6:
        exit()
    
    else:
        clear_terminal()
        print('Некорректный выбор!',end="\n"*2)


main()
#сделать проверки на ввод веса, роста, по возможности сделать цикл нормальный 
#при изменении роста или веса проверять на (число и не пустую строку), затем\
#вызывать def calc_bmi и меня его тоже
