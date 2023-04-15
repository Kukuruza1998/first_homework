import os

#печатает меню из другого файла +
def print_menu():
  file = open('calc_bmi_with_read_write_another_file/menu.txt', encoding='utf-8')
  for i in file:
    print(i.strip())
  file.close()  

#очищаем терминал +
def clear_screen():
  os.system('CLS')

#проверяет что выбрал пользователь 1...6 или неверный ввод +
def processing_user_choice_menu():
  a = input("Ваш выбор: ")
  if a.isdigit():
    a = int(a)
    if 1 <= a <= 6:
      return a
  clear_screen()
  print('Некорректный выбор!',end="\n"*2)

#запускает функцию согласно выбору пользователя +
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

#печатает ид всех пользователей из стороннего файла +
def print_all_id_user():
  file = open('calc_bmi_with_read_write_another_file/person_info.txt', encoding='utf-8')
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
 
#печатает полную информацию о данном пользователе из стороннего файла -  если нет логина то "нет логина"
def print_info_about_user():
  a = input('Введите логин пользователя, которого хотите посмотреть: ')

  file = open('calc_bmi_with_read_write_another_file/person_info.txt', encoding='utf-8')
  lines = file.readlines()
  a = f"1) Логин: {a}\n"
  clear_screen()
  for line in lines:
    if a == line:
      x = 0
      while x!=6:
        print(lines[lines.index(line)+x], end="")
        x +=1
      print()
    
    
#изменение информации о выбранном пользователе в стороннем файле
def change_ifno_about_user():
  pass

#удаляет выбранного пользователя в стороннем файле
def delete_selected_user():
  a = input('Введите логин пользователя, которого хотите удалить: ')

  file = open('calc_bmi_with_read_write_another_file/person_info.txt','r', encoding='utf-8')
  lines = file.readlines()
  a = f"1) Логин: {a}\n"

  for line in lines:
    if a == line:
      s = ''
      _index = lines.index(line)
      for i in range(_index, _index + 7):
        lines[i] = s

  file = open('calc_bmi_with_read_write_another_file/person_info.txt','w', encoding='utf-8')
  file.writelines(lines)
  file.close()

	
#очищает файл от пустых строк, после удаления+
# def remove_empty_str(a):
#   try:
#     while True:
#       a.remove('')
#   except ValueError:
#       pass    

#добавляет пользователя в сторонний файл+
def add_user_in_dict():
  clear_screen()
  _login = input(f"Введите логин пользователя(not ''): ")
  _gender = input(f"Введите пол пользователя(male/female): ")
  _age = input(f"Введите возраст пользователя(1...99): ") 
  _height = input(f"Введите рост пользователя(1...250 см): ")
  _weight = input(f"Введите вес пользователя(1...200 кг): ")
  if validation_input_info_about_user\
    (_login, _gender, _age, _height, _weight) == True:

    file = open('calc_bmi_with_read_write_another_file/person_info.txt','a', encoding='utf-8')
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

#проверяет правильность ввода информации о пользователе +
def validation_input_info_about_user(a, b, c, d, e):
  if not a =="":
    if  b == 'male' or  b == 'female':
      if c.isdigit() and c !="" and 0 < int(c) < 100:
        if  d.isdigit() and 0 < int(d) < 251 and not d == "":  
          if  e.isdigit() and 0 < int(e) < 201 and not e == "":
            return True

#окончание работы калькулятора+
def exit_with_calc():
  exit()

def main():
  clear_screen()
  while True:
    print_menu()
    start_func_for_menu_item(processing_user_choice_menu())
    
main()