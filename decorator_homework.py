import os, random

def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        value = f"Итоговая сумма Вашего счёта: ${func(*args, **kwargs)}"
        return value
    return wrapper_decorator

@decorator
def adds(b = 0):
    a = random.randint(0, 10000)
    if b != 0:
      print(f"Сумма до пополнения: ${a}")
    return a + b

os.system('CLS')
login_person = input('Введите свой логин: ').lower()

if (login_person == 'admin'):
    money = input("Введите сумму, которую хотели бы положить на счёт: $")
    if money != "" and money.isdigit():
      print(adds(int(money)))
    else:
      print(adds())   
else:
    print('Доступ запрещен')