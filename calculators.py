import operator

import messages
from libs.os import clear
from libs.io import get_numbers, get_arithmetic_operators

arithmetic_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
    '//': operator.floordiv,
}


def _mathematical_on_lists(numbers: list, oper: str) -> float:
    if len(numbers) == 2:
        return arithmetic_operators[oper](numbers[0], numbers[1])
    else:
        last_number = numbers.pop()
        return arithmetic_operators[oper](_mathematical_on_lists(numbers, oper), last_number)


def simple_calculator():
    clear()
    numbers = get_numbers(float, 2)
    try:
        oper = get_arithmetic_operators()
    except:
        clear()
        print(messages.call_function_error)
    else:
        result = _mathematical_on_lists(numbers, oper)
        clear()
        print("The result is: ", result)
    

def multiple_numbers_calculator():
    clear()
    print("multiple_numbers_calculator")