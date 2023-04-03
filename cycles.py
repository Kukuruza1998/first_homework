from array import *
import operator


test_int = 5

while test_int > 0:
        print(f"Наша переменная равна: {test_int}")
        test_int -= 2




data = array('i', [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

print(f"\nВыведите все элементы, которые меньше 5: \
{[i for i in data if i < 5]}", end="\n"*2)




a = array('i', [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) 
b = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

result = [i for i in a if i in b]
print(f"Нужно вернуть список, который состоит из элементов, общих \
для этих двух списков: {result}", end="\n"*2)




c = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(f"Отсортируйте словарь по значению в порядке возрастания: \
{dict(sorted(c.items(), key=operator.itemgetter(1)))}")
print(f"Отсортируйте словарь по значению в порядке убывания: \
{dict(sorted(c.items(), key=operator.itemgetter(1), reverse=True))}")