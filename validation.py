def isfloat(input_user: str) -> bool:
    """A function to check whether the user's input is float.

    Args:
        input_user (str): The value entered by the user, which is generally of the string type.

    Returns:
        bool: If the passed value is float, it returns True.
    """
    input_user = input_user.split('.')
    if len(input_user) == 2:
        if input_user[0].isnumeric() and input_user[1].isnumeric():
            return True
    return False

def is_arithmetic_operators(char: str) -> bool:
    """_summary_

    Args:
        char (str): _description_

    Returns:
        bool: _description_
    """
    operators = ('+', '-', '*', '/', '%', '**', '//')
    if char in operators:
        return True
    else:
        return False
