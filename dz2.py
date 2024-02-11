import re
from typing import Callable


def generator_numbers(text):
    pattern="(\d*\.\d*)"
    for char in text.split():
        if re.match(pattern,char):
            yield char
        else:
            continue
        

def sum_profit(text: str, func: Callable):
    summ=0
    for el in generator_numbers(text):
        summ+=float(el)
    return summ

