BMI = float(input('Weight: ')) / float(input('Hight: '))**2 

d = ['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=']
d[round((round(BMI)-21)/3)] = '|'

print('BMI = '+str(round(BMI))+'\n20 '+''.join(d)+' 56')