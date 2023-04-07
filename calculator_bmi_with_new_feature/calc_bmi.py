""" пол, вес, возраст. Выводим рекомендации в зависимости от bmi """

value_infinite_loop = True

while (value_infinite_loop):
  if input('quit the calculator? ()') == 'y':
    break

  else:
    bmi = float(input('Enter weaght(kg): ')) / (float(input('Enter height(cm): '))*0.01)**2

    chart_bmi =  '========================'


    if 16 >= round(bmi):
      print('BMI is too small'+"\n"*3)

    elif round(bmi) < 40:
      li = list(chart_bmi)
      li[round(bmi) - 17] = '|'

      print(f"BMI = {round(bmi)}")
      print(f"16{''.join(li)}40"+"\n"*3)

    else:
      print('BMI is too big'+"\n"*3)