import os

def print_menu():
  file = open('calc_bmi_read_write_another_file/menu.txt', encoding='utf-8')
  for i in file:
    print(i.strip())
  file.close()  

def clear_screen():
  os.system('CLS')

def processing_user_choice_menu():
  a = input("Ваш выбор: ")
  if a.isdigit():
    a = int(a)
    if 1 <= a <= 6:
      return a
  clear_screen()
  print('Некорректный выбор!',end="\n"*2)

def start_func_for_menu_item(a):
  if a==1:
    print_all_id_user()
  elif a==2:
    print_all_id_user()
    print_info_about_user()
  elif a==3:
    print_all_id_user()
    change_ifno_about_user()
  elif a==4:
    print_all_id_user()
    delete_selected_user()
  elif a==5:
    add_user_in_dict()
  elif a==6:
    exit_with_calc()

def print_all_id_user():
  file = open('calc_bmi_read_write_another_file/person_info.txt', encoding='utf-8')
  lines = file.readlines()
  count_lines = 0
  clear_screen()
  for i in lines:
    if i[:2] == '1)':
      print(f"Пользователь: {i[10:]}", end='')
      count_lines += 1

  if count_lines == 0:
    clear_screen()
    print('Пользователей не зарегистрировано')
  print() 
  file.close()    
 
def print_info_about_user():
  a = input('Введите логин пользователя, которого хотите посмотреть: ')

  file = open('calc_bmi_read_write_another_file/person_info.txt', encoding='utf-8')
  lines = file.readlines()
  a = f"1) Логин: {a}\n"
  x = 0
  clear_screen()
  for line in lines:
    if a == line:
      while x!=6:
        print(lines[lines.index(line)+x], end="")
        x +=1
      print()
  file.close()
  if x == 0:
    print('Данного пользователя не существует', end='\n'*2)
    
def change_ifno_about_user():
  a = input('Введите логин пользователя, которого хотите изменить: ')
  file = open('calc_bmi_read_write_another_file/person_info.txt','r', encoding='utf-8')
  lines = file.readlines()
  a = f"1) Логин: {a}\n"
  x=0
  for line in lines:
    if a == line:
      while x!=6:
        print(lines[lines.index(line)+x], end="")
        x +=1
      print()
      change_param = input('Введите ключ, который хотите изменить: ')
      _index_to_change = check_param_to_change(change_param)
      if _index_to_change != False:
        _index = lines.index(line)
        if _index_to_change == 0:
          lines[_index+_index_to_change] = f"1) Логин: {input('Введите значение: ')}\n"
        elif _index_to_change == 1:
          lines[_index+_index_to_change] = f"2) Пол: {input('Введите значение: ')}\n"
        elif _index_to_change == 2:
          lines[_index+_index_to_change] = f"3) Возраст: {input('Введите значение: ')}\n"
        elif _index_to_change == 3:
          lines[_index+_index_to_change] = f"4) Рост: {input('Введите значение: ')}\n"
        elif _index_to_change == 4:
          lines[_index+_index_to_change] = f"5) Вес: {input('Введите значение: ')}\n"
        elif _index_to_change == 5:
          lines[_index+_index_to_change] = f"6) ИМТ: {input('Введите значение: ')}\n"
  file.close()
  if x == 0:
    print('Данного пользователя не существует', end='\n'*2)
  else:
    clear_screen()
    print('Пользователь изменён', end='\n'*2)


      # s = ''
      # _index = lines.index(line)
      # for i in range(_index, _index + 7):
      #   lines[i] = s

    file = open('calc_bmi_read_write_another_file/person_info.txt','w', encoding='utf-8')
    file.writelines(lines)
    file.close()
  
def check_param_to_change(a):
  if f"1) {a}" == '1) Логин':
    return 0
  elif f"2) {a}" == '2) Пол':
    return 1
  elif f"3) {a}" == '3) Возраст':
    return 2
  elif f"4) {a}" == '4) Рост':
    return 3
  elif f"5) {a}" == '5) Вес':
    return 4
  elif f"6) {a}" == '6) ИМТ':
    return 5
  else: return False

def delete_selected_user():
  a = input('Введите логин пользователя, которого хотите удалить: ')

  file = open('calc_bmi_read_write_another_file/person_info.txt','r', encoding='utf-8')
  lines = file.readlines()
  a = f"1) Логин: {a}\n"

  for line in lines:
    if a == line:
      s = ''
      _index = lines.index(line)
      for i in range(_index, _index + 7):
        lines[i] = s

  file = open('calc_bmi_read_write_another_file/person_info.txt','w', encoding='utf-8')
  file.writelines(lines)
  file.close()
  clear_screen()
  print('Пользователь удалён', end='\n'*2)

def add_user_in_dict():
  clear_screen()
  _login = input(f"Введите логин пользователя(not ''): ")
  _gender = input(f"Введите пол пользователя(male/female): ")
  _age = input(f"Введите возраст пользователя(1...99): ") 
  _height = input(f"Введите рост пользователя(1...250 см): ")
  _weight = input(f"Введите вес пользователя(1...200 кг): ")
  if validation_input_info_about_user\
    (_login, _gender, _age, _height, _weight) == True:

    file = open('calc_bmi_read_write_another_file/person_info.txt','a', encoding='utf-8')
    file.write(f"1) Логин: {_login}\n")
    file.write(f"2) Пол: {_gender}\n")
    file.write(f"3) Возраст: {_age}\n")
    file.write(f"4) Рост: {_height}\n")
    file.write(f"5) Вес: {_weight}\n")
    file.write(f"6) ИМТ: {round(float(_weight)/((float(_height)*0.01)**2))}\n")
    file.write("\n")
    file.close()
    clear_screen()
  else:
    print('Некоректное заполнение данных')

def validation_input_info_about_user(a, b, c, d, e):
  if not a =="":
    if  b == 'male' or  b == 'female':
      if c.isdigit() and c !="" and 0 < int(c) < 100:
        if  d.isdigit() and 0 < int(d) < 251 and not d == "":  
          if  e.isdigit() and 0 < int(e) < 201 and not e == "":
            return True

def exit_with_calc():
  exit()

def main():
  clear_screen()
  while True:
    print_menu()
    start_func_for_menu_item(processing_user_choice_menu())
    
main()