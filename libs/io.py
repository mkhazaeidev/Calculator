import messages
from libs.os import clear
from validation import is_arithmetic_operators


def convert_str_list_to_numbers_list(numbers_type: type, numbers: str):
    if numbers_type in (int,  float, complex):
        numbers = numbers.split()
        try:
            return [numbers_type(number) for number in numbers if number]
        except:
            raise ValueError("Some element are not Number.")
    else:
        raise TypeError("The type must be in (int, float, complex).")


def get_input(prompt: str) -> str:
    """A function to receive input from the user.

    Args:
        prompt (str): A message displayed to the user for input.

    Returns:
        str: Return value from standard input.
    """
    return input(prompt.capitalize() + ": ")


def get_numbers(number_type: type, count: int) -> list:
    """A function to get a set of numbers.

    Args:
        number_type (type): Specifies the numeric data type.
        count (int): Specifies the count of input numbers.

    Returns:
        list: Returns the list of input numbers.
    """
    acceptable_types = [int, float, complex]
    numbers = []
    index = 0
    error = False
    if number_type in acceptable_types:
        while index < count:
            clear()
            print("You must enter {} \"{}\" numbers".format(count, number_type.__name__))
            if error:
                print("Warning: You did not enter number {} correctly. Please try again.".format(index + 1))
                error = False
            number = input(f"{index + 1}. ")
            try:
                numbers.append(number_type(number))
            except:
                error = True
            else:
                index += 1
    else:
        raise ValueError(f"The type sent is not acceptable. The type must be one of {[item.__name__ for item in acceptable_types]}.")

    return numbers

def get_arithmetic_operators():
    error_counter = 0
    operator = ''
    while True:
        operator = get_input(messages.get_operators)
        if is_arithmetic_operators(operator):
            return operator
        else:
            if error_counter < 4:
                print(messages.get_operators_error)
                error_counter += 1
            else:
                break
    raise ValueError


def get_numbers_inline():
    while True:
        numbers = input("Please separate the numbers with a space and then press enter:\n")
        try:
            return convert_str_list_to_numbers_list(float, numbers)
        except Exception as e:
            print(e)
    

