import os, random

from card import card_list
deck = card_list.card_list

def clear_Screen():
    os.system("CLS")

def check_card_in_deck():
    if not deck:
      print('Карты в колоде закончились',end='\n'*2)
      exit()
    
    return check_on_ace()

def check_on_ace():
    card_input = deck.pop(random.randint(0, len(deck)-1))
    if card_input == 1:
      print(f"Пришёл туз, добавим 11 или 1?")
      ace = input()
      if ace == '1':
          card_input = int(ace)
      elif ace == '11':
          card_input = int(ace)
    
    return card_input
           

def print_a_card(count_el_card):
    card_adds = check_card_in_deck()
    count_el_card += card_adds
    print(f"Пришла: {card_adds}. Итого: {count_el_card}")
    check_on_21(count_el_card)

def check_on_21(count_el_cards):
    if count_el_cards < 21:
      check_to_add_more_card(count_el_cards)
    elif count_el_cards == 21:
      print('Победа, 21 очко',end='\n'*2)
      exit
    else:
      clear_Screen()
      print(f"Перебор, итог: {count_el_cards}",end='\n'*2)
      return exit

def check_to_add_more_card(count_el_card):
    ask_add_card = input('Взять карту(y/n)? ')
    if ask_add_card == "y":
      print_a_card(count_el_card)
      
    elif ask_add_card == "n":
      clear_Screen()
      print(f"Ваш результат: {count_el_card}",end='\n'*2)
      return exit
    else:
      clear_Screen()
      print('Научись тыкать на буквы',end='\n'*2)

def main():
    clear_Screen()
    while True:
      first_card = check_card_in_deck()
      second_card = check_card_in_deck() 
      print(f"Первой пришла карта номиналом: {first_card}, вторая: {second_card}")
      if (first_card == 1 or first_card == 11) and (second_card == 1 or second_card == 11):
        print("Победа, два туза")
        exit 
      else:
        print(f"Итого: {first_card + second_card}")
        check_on_21(first_card + second_card)


if __name__ == "__main__":
    main()