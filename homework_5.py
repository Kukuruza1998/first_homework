A = [ int(input(f"Напишите {i+1} значение: ")) for i in range(3) ]
zero = int(0)

print(f"Наши значения: {A}")

# №1  
print(A[0]and A[1]and A[2] and "Нет нулевых значений!!!")

# №2
print(A[0] or A[1] or A[2] or "Введены все нули!")

# №3
if A[0] >  A[1] + A[2]:
  if A[1] < 0 and A[2] < 0:
    print(f"a - b - c = {A[0] + A[1] + A[2]}")
  elif list(A)[2] < 0:
    print(f"a - b - c = {A[0] - A[1] + A[2]}")
  else:
    print(f"a - b - c = {A[0] + A[1] - A[2]}")

# №4
if A[0] <  A[1] + A[2]:
  print(f"b + c - a = {-A[0] + A[1] + A[2]}")  