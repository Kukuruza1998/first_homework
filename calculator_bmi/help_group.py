BMI = float(input('Weight: ')) / float(input('Hight: '))**2 

d = ['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=']
d[round((round(BMI)-17)/2)] = '|'



if round(BMI) < 16:
  print('BMI is too small')

elif round(BMI) < 40:
  print(f"BMI = {round(BMI)} \n16 {''.join(d)} 40")

else:
  print('BMI is too big')
