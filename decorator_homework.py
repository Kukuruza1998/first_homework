import os, random

def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        value = f"Итоговая сумма Вашего счёта: ${func(*args, **kwargs)}"
        return value
    return wrapper_decorator

@decorator
def adds(a, b = 0):
    return a + b

os.system('CLS')
login_person = input('Введите свой логин: ').lower()
total_money = random.randint(0, 10000)
if (login_person == 'admin'):
    money = input("Введите сумму, которую хотели бы положить на счёт: $")
    if money != "" and money.isdigit():
      print(f"Сумма до пополнения: ${total_money}")
      print(adds(int(money), total_money))
    else:
      print(adds(total_money))   
else:
    print('Доступ запрещен')