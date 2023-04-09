A = [ int(input(f"Напишите {i+1} значение: ")) for i in range(3) ]
zero = int(0)

print(f"Наши значения: {A}")

# №1
for i in range (1):
  while A[i] and A[i+1] and A[i+2]:
    print("Нет нулевых значений!!!")
    break
    

# №2
print(list(A)[0] or list(A)[1] or list(A)[2] or "Введены все нули!")

# №3
if list(A)[0] >  list(A)[1] + list(A)[2]:
  if list(A)[1] < 0 and list(A)[2] < 0:
    print(f"a - b - c = {list(A)[0] + list(A)[1] + list(A)[2]}")
  elif list(A)[2] < 0:
    print(f"a - b - c = {list(A)[0] - list(A)[1] + list(A)[2]}")
  else:
    print(f"a - b - c = {list(A)[0] + list(A)[1] - list(A)[2]}")

# №4
if list(A)[0] <  list(A)[1] + list(A)[2]:
  if list(A)[1] < 0 and list(A)[2] < 0:
    print(f"b + c - a = {-list(A)[0] + list(A)[1] + list(A)[2]}")
  elif list(A)[2] < 0:
    print(f"b + c - a = {-list(A)[0] + list(A)[1] + list(A)[2]}")
  else:
    print(f"b + c - a = {-list(A)[0] + list(A)[1] + list(A)[2]}")  