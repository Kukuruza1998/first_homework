_state={0:{'id':'a',
           'age':'12',
           'name':'123',
           'gender':'male'},
        1:{'id':'b',
           'age':'12',
           'name':'123',
           'gender':'male'}, 
        2:{'id':'c',
           'age':'12',
           'name':'123',
           'gender':'male'},
        3:{'id':'d',
           'age':'12',
           'name':'123',
           'gender':'male'},  
           }


def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)['id']
        return (value) 
    return wrapper_decorator

@decorator
def print_menu(state):
     while True:
      for key, value in state.items():  
          return value
      break
          

print(print_menu(_state))

change_parameter = \
              input('Введите название ключа которое хотите изменить: ')
for x in print_menu(_state):
    if change_parameter==x:
                 print_menu(_state)[x]=input('Введите значение: ')

print(print_menu(_state))