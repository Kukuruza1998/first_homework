import sys

list1=['foo', 'foo','foo','foo', ]
list2=['fso','fso','fso']

a = [1, 2, 3]
b = 1, 2, 3



print(sys.getsizeof(a))
print(sys.getsizeof(b))


print(list1+list2)
list2+='string'
print(list2)