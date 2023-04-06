a = input('Enter height(cm): ')
b = input('Enter weaght(kg): ')
bmi = float(b) / (float(a)*0.01)**2

chart_bmi =  '========================'


if 16 >= round(bmi):
  print('BMI is too small')

elif round(bmi) < 40:
  li = list(chart_bmi)
  li[round(bmi) - 17] = '|'

  print(f"BMI = {round(bmi)}")
  print(f"16{''.join(li)}40")

else:
  print('BMI is too big')