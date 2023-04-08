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

# Slim male
    elif round(bmi) > 16 and round(bmi) < 25: 
        li = list(chart_bmi)
        li[round(bmi) - 17] = '|'

        #block  16-24bmi male 0-55y, 55-122y
        if person_gender == 'male':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI in normal position for before 55 male year")
          
          #block  16-24bmi male 0-55y, 55-122y
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position for after 55 male year')

          #block  16-24bmi male 0-55y, 55-122y
          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position for male')

        elif person_gender == 'female':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI in normal position for before 55 female year")
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position for after 55 female year')

          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position for female')

        else:
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position for before 55 year')
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position for after 55 year')

          else:
            print(f"\nBMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI in normal position') 

# Plump male
    elif round(bmi) > 24 and round(bmi) < 33: 
        li = list(chart_bmi)
        li[round(bmi) - 17] = '|'

        if person_gender == 'male':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI is elevated for male under 55")
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated for male over 55')

          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated for male')

        elif person_gender == 'female':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI is elevated for female under 55")
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated for female over 55')

          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated for female')

        else:
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated for under 55')
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated for over 55')

          else:
            print(f"\nBMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is elevated') 

# Fatty male
    elif round(bmi) > 32 and round(bmi) < 40: 
        li = list(chart_bmi)
        li[round(bmi) - 17] = '|'

        if person_gender == 'male':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI is critical for male under 55")
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for male over 55')

          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for male')

        elif person_gender == 'female':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI is critical for female under 55")
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for female over 55')

          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for female')
            
        else:
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for under 55')
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for over 55')

          else:
            print(f"\nBMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical') 



# Fatty female
    elif round(bmi) > 32 and round(bmi) < 40: 
        li = list(chart_bmi)
        li[round(bmi) - 17] = '|'

        if person_gender == 'female':
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print("\nYour BMI is critical for female under 55")
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"Gender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for female over 55')

          else:
            print(f"\nGender = {person_gender}")
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for female')
        else:
          if person_age.isdigit() and int(person_age) < 56:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for under 55')
          
          elif person_age.isdigit() \
                and int(person_age) > 55 and int(person_age) < 123:
            print(f"\nAge = {person_age}")  
            print(f"BMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical for over 55')

          else:
            print(f"\nBMI = {round(bmi)}")
            print(f"16{''.join(li)}40")

            print('\nYour BMI is critical')

    else:
      print('BMI is too big'+"\n")       