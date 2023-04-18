import time
import os
from datetime import datetime

from view_number import views


def clear_screen():
    os.system("CLS")

def get_view(number: str):
    first = None
    second = None
    if len(number) == 1:
        first = views.NUMBER_TO_VIEW["0"]
        second = views.NUMBER_TO_VIEW[number]
    else:
        first = views.NUMBER_TO_VIEW[number[0]]
        second = views.NUMBER_TO_VIEW[number[1]]
    return combine_views(first, second)

def combine_views(first, second):
    combine_numbers = [f"{first_}  {second_}" for first_, second_ in zip\
         (first.splitlines(), second.splitlines())]
    result = "\n".join(i for i in combine_numbers)
    return result

if __name__ == '__main__':
    counter = 1
    while True:
        clear_screen()
        current_time = datetime.now().time()
        hour_views = get_view(str(current_time.hour))
        minute_views = get_view(str(current_time.minute))
        second_views = get_view(str(current_time.second))

        if counter % 4 == 0:
          result = combine_views(hour_views, views.NUMBER_TO_VIEW[":"])
          result = combine_views(result, minute_views)
          result = combine_views(result, views.NUMBER_TO_VIEW[":"])
          result = combine_views(result, second_views)
          print(result)
        else:
          result = combine_views(hour_views, views.NUMBER_TO_VIEW["nothing"])
          result = combine_views(result, minute_views)
          result = combine_views(result, views.NUMBER_TO_VIEW["nothing"])
          result = combine_views(result, second_views)
          print(result)  

        time.sleep(0.2)
        counter += 1
#
# def print_time(a=two, b=four, d=one, e=zero, c=dot, f=empty):
#     result = ""
#     # print( a, b, d, e)
#     for line_a, line_b, line_c, line_d, line_e, line_f in zip(
#         a.splitlines(),
#         b.splitlines(),
#         c.splitlines(),
#         d.splitlines(),
#         e.splitlines(),
#         f.splitlines(),
#     ):
#
# while True:
#     pime = datetime.now()
#     os.system("clear")
#     counter += 1
#     print(pime.strftime("%I:%M:%S%p"))
#     check_time(counter, pime.strftime("%M%S"))
#
#     time.sleep(1)
