import os, random

from card import card_list


def clear_Screen():
    os.system("CLS")

def check_card_in_deck():
    if len(card_list.card_list)-1 == 0:
      print('Карты в колоде закончились',end='\n'*2)
      exit()
    return card_list.card_list.pop(random.randint(1, len(card_list.card_list)-1))

def check_to_more(count_el_card):
    if count_el_card <= 21:
      ask_add_card = input('Взять карту(y/n)? ')
      if ask_add_card == "y":
        card_adds = check_card_in_deck()
        count_el_card += card_adds

        print(f"Пришла: {card_adds}. Итого: {count_el_card}")
        check_to_more(count_el_card)
      elif ask_add_card == "n":
        clear_Screen()
        print(f"Ваш результат: {count_el_card}",end='\n'*2)
        return exit
      else:
        clear_Screen()
        print('Научись тыкать на буквы',end='\n'*2)
    else:
        clear_Screen()
        print(f"Перебор, итог: {count_el_card}",end='\n'*2)
        return exit

def main():
    clear_Screen()
    while True:
      input_card = check_card_in_deck()
      second_card = check_card_in_deck() 
      print(f"Первой пришла карта номиналом: {input_card}, второй: {second_card}")
      if (input_card == 1 or input_card == 11) and (second_card == 1 or second_card == 11):
        print("Победа, два туза")
        exit 
      else:
        print(f"Итого: {input_card + second_card}")
        check_to_more(input_card + second_card)


if __name__ == "__main__":
    main()