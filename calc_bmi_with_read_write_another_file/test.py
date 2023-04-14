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

#печатает ид всех пользователей из стороннего файла
def print_all_id_user():
  file = open('calc_bmi_with_read_write_another_file/person_info.txt', encoding='utf-8')
  lines = file.readlines()
  for i in lines:
    print(file.read(3))

#печатает полную информацию о данном пользователе из стороннего файла
def print_info_about_user():
  pass

#изменение информации о выбранном пользователе в стороннем файле
def change_ifno_about_user():
  pass

#удаляет выбранного пользователя в стороннем файле
def delete_selected_user():
  pass

#добавляет пользователя в сторонний файл
def add_user_in_dict():
  validation_input_info_about_user()

#проверяет правильность ввода информации о пользователе
def validation_input_info_about_user():
  pass

#окончание работы калькулятора
def exit_with_calc():
  exit()



def main():
  while True:
    clear_screen()#+
    print_menu()#+
    start_func_for_menu_item(processing_user_choice_menu())
    break





main()