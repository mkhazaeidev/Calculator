from oslib import clear

def get_input(prompt: str) -> str:
    """_summary_

    Args:
        prompt (str): _description_

    Returns:
        str: _description_
    """
    return input(prompt + ": ").capitalize()

def get_numbers(number_type: type, count: int) -> list:
    numbers = []
    index = 0
    error = False
    while index < count:
        clear()
        print("You must enter {} {} numbers".format(count, number_type))
        if error:
            print(f"Warning: You did not enter number {index + 1} correctly. Please try again.")
            error = False
        number = input(f"{index + 1}. ")
        try:
            numbers.append(number_type(number))
            index += 1
        except:
            error = True
        
    return numbers
        