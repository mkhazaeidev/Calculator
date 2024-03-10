import messages
import fixtures
from validation import user_confirm, come_agian, check_user_selection
from libs.io import get_input
from libs.sort import sort_menu_by_order
from libs.os import clear


# import menu and sort it.
menu_items = sort_menu_by_order(fixtures.menu_items)
options_list = [str(item) for item in range(1, len(menu_items)+1)]


def menu(menu_items: dict):
    """A function to display a dictionary with a specific structure.

    Args:
        menu_items (dict): A dictionary whose keys are the names of existing functions.
        And its value is a dictionary with three keys name, description and order.

    example:
    {
        "simple_calculator": {
            "name": "Simple Calculator",
            "description": "Simple calculator with two inputs",
            "order": 3,
        },

        "multiple_numbers_calculator": {
            "name": "Multiple numbers Calculator",
            "description": "Performs a mathematical operation on multiple numbers",
            "order": 2,
        }
    }
    """
    index = 1
    for key in menu_items:
        print(f"\t{index}. ", menu_items[key]['name'])
        print(f"\t\tHelp text: {menu_items[key]['description']}\n")
        index += 1
    print("\te. Exit\n")


def return_menu_function_name(user_selection, options_list) -> str:
    zip_menu = dict(zip(options_list, list(menu_items.keys())))
    return zip_menu[user_selection]


def call_menu_function(function_name: str):
    import calculators
    func = getattr(calculators, function_name)
    func()


def main():
    error = False
    clear()
    print(messages.program_title)
    char = input(messages.start_the_program)

    if user_confirm(char):
        while True:
            clear()

            if error:
                print("Error: ", messages.incorrect_choice)
                error = False

            print(messages.menu_title)
            menu(menu_items)
            user_selection = get_input(messages.select_menu)

            if user_selection == 'e':
                clear()
                print(messages.end_the_program)
                break
            elif check_user_selection(user_selection, options_list):
                function_name = return_menu_function_name(user_selection, options_list)
                call_menu_function(function_name)

                if not come_agian(messages.continue_the_program):
                    clear()
                    print(messages.end_the_program)
                    break
            else:
                error = True

    else:
        clear()
        print(messages.end_the_program)


if __name__ == "__main__":
    main()

