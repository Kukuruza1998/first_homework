from datetime  import datetime  
import time, os


one="""
    ■■■   
  ■■■■■   
    ■■■   
    ■■■   
    ■■■   
■■■■■■■■■■
"""

two="""
  ■■■■■■  
■■■    ■■■
     ■■■■ 
   ■■■■   
 ■■■■     
■■■■■■■■■■
"""

three="""
■■■■■■■■■■
        ■■
■■■■■■■■■■
        ■■
        ■■
■■■■■■■■■■
"""

four="""
■■      ■■
■■      ■■
■■■■■■■■■■
        ■■
        ■■
        ■■
"""

five="""
■■■■■■■■■■
■■        
■■■■■■■■■■
        ■■
        ■■
■■■■■■■■■■
"""

six="""
■■■■■■■■■■
■■        
■■■■■■■■■■
■■      ■■
■■      ■■
■■■■■■■■■■
"""

seven="""
■■■■■■■■■■
        ■■
      ■■■ 
    ■■■   
    ■■■   
    ■■■   
"""

eight="""
■■■■■■■■■■
■■      ■■
■■■■■■■■■■
■■      ■■
■■      ■■
■■■■■■■■■■
"""

nine="""
■■■■■■■■■■
■■      ■■
■■      ■■
■■■■■■■■■■
        ■■
■■■■■■■■■■
"""

zero="""
  ■■■■■■  
 ■■    ■■ 
■■      ■■
■■      ■■
 ■■    ■■ 
  ■■■■■■  
"""

dot="""
    ■■    
    ■■    
          
          
    ■■    
    ■■    
"""

empty="""
          
          
          
          
          
          
"""

def print_time( a=two, b=four, d=one, e=zero, c=dot, f=empty):
  result = ''
  # print( a, b, d, e)
  for line_a, line_b, line_c, line_d, line_e, line_f in zip(a.splitlines(), \
                                                    b.splitlines(), \
                                                    c.splitlines(), \
                                                    d.splitlines(), \
                                                    e.splitlines(), \
                                                    f.splitlines()):
    if counter % 5 == 0:
      result += line_a + '  ' + line_b + '  ' + line_c + '  ' + line_d + '  ' + line_e + '\n'
    else:
      result += line_a + '  ' + line_b + '  ' + line_f + '  ' + line_d + '  ' + line_e + '\n' 
  print(result)


counter = 1  
def check_time(counter, time_now):
  a = ''
  b = ''
  d = ''
  e = ''
  for i in time_now:
    if int(i) == 0:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 1:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 2:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 3:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 4:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 5:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 6:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 7:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 8:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
    elif int(i) == 9:
      if a == '':
        a = i
      elif b == '':
        b = i
      elif d == '':
        d = i
      elif e == '':
        e = i
  print_number( a, b, d, e)
    




while True:
  pime = datetime.now()
  os.system('CLS')
  counter += 1
  print(pime.strftime("%I:%M:%S%p"))
  check_time(counter, pime.strftime("%M%S"))

  time.sleep(1)