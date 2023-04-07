""" пол, вес, возраст. Выводим рекомендации в зависимости от bmi """

value_infinite_loop = True

while (value_infinite_loop):
  if input("""\n               quit the calculator? 
      ('q' to exit, any input for continue):\n""").lower() == 'q':
    break

  else:
    person_gender = input('Enter your gender (male/female): ').lower()
    person_age = (input('Enter your age: '))
    bmi = float(input('Enter weaght(kg): ')) /\
          (float(input('Enter height(cm): '))*0.01)**2 
    chart_bmi =  '========================'


    if 16 >= round(bmi):
      print('BMI is too small'+"\n")

    elif round(bmi) < 40:
        li = list(chart_bmi)
        li[round(bmi) - 17] = '|'

        if person_gender == 'male' or person_gender == 'female':
          if person_age.isdigit() and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            """  """
          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            """  """
        else:
          if person_age.isdigit() and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            """  """
          else:
            print(f"\nBMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            """  """

    else:
      print('BMI is too big'+"\n")       