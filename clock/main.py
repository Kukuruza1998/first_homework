import time
import os
from datetime import datetime
from colorama import init, Fore, Style

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

def main():
    init()
    COLORS_FOR_PRINT = [Fore.YELLOW, \
                        Fore.BLUE, \
                        Fore.GREEN, \
                        Fore.MAGENTA, \
                        Fore.WHITE,
                        Fore.CYAN
                        ]
    counter_position = 1
    index_to_colors = 0
    while True:
        color_print = COLORS_FOR_PRINT[index_to_colors]
        if counter_position == 6: 
          step = -1
        elif counter_position == 1:
          step = 1
        
        clear_screen()
        current_time = datetime.now().time()
        hour_views = get_view(str(current_time.hour))
        minute_views = get_view(str(current_time.minute))
        second_views = get_view(str(current_time.second))
        
        result = combine_views(hour_views, \
                               views.NUMBER_TO_VIEW["position_square"]\
                                [counter_position])
        result = combine_views(result, minute_views)
        result = combine_views(result, \
                               views.NUMBER_TO_VIEW["position_square"]\
                                [counter_position])
        result = combine_views(result, second_views)  
        print(color_print + result)

        counter_position += step
        index_to_colors = (index_to_colors + 1) % len(COLORS_FOR_PRINT)
        time.sleep(1)

if __name__ == '__main__':
    main()