from libs.os import clear


def get_input(prompt: str) -> str:
    """A function to receive input from the user.

    Args:
        prompt (str): A message displayed to the user for input.

    Returns:
        str: Return value from standard input.
    """
    return input(prompt + ": ").capitalize()


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
