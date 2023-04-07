""" пол, вес, возраст. Выводим рекомендации в зависимости от bmi """

value_infinite_loop = True

while (value_infinite_loop):
  if input("""\n               quit the calculator? 
      ('q' to exit, any input for continue):\n""").lower() == 'q':
           
    break

  else:
    person_gender = input('Enter ur gender (male/female): ').lower()
    bmi = float(input('Enter weaght(kg): ')) / (float(input('Enter height(cm): '))*0.01)**2

    chart_bmi =  '========================'


    if 16 >= round(bmi):
      print('BMI is too small'+"\n"*2)

    elif round(bmi) < 40:
      li = list(chart_bmi)
      li[round(bmi) - 17] = '|'

      if person_gender == 'male' or 'female':
        print(f"\nGender = {person_gender}")
        print(f"BMI = {round(bmi)}")
        print(f"16{''.join(li)}40"+"\n"*2)
      else:
        print(f"\nBMI = {round(bmi)}")
        print(f"16{''.join(li)}40"+"\n"*2)

    else:
      print('BMI is too big'+"\n"*3)