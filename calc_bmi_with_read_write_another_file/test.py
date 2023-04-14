import os

#печатает меню из другого файла
def print_menu():
  for i in open("/calc_bmi_with_read_write_another_file/menu.txt"):
    print(i.strip())

#очищаем терминал
def clear_screen():
  os.system('CLS')


#проверяет что выбрал пользователь 1...6 или неверный ввод
def processing_user_choice_menu():
  pass

#запускает функцию согласно выбору пользователя
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
  pass

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
    clear_screen()
    print_menu()
    processing_user_choice_menu()
    start_func_for_menu_item()
    break





main()