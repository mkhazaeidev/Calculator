import messages
import fixtures
from validation import user_confirm
from lib.io import get_input
from lib.sort import sort_menu_by_order
from lib.os import clear


# import menu and sort it.
menu_items = sort_menu_by_order(fixtures.menu_items)
options_list = [str(item) for item in range(1, len(menu_items)+1)]

def menu(menu_items: dict):
    index = 1
    for key in menu_items:
        print(f"{index}. ", menu_items[key]['name'])
        index += 1
        
def check_user_selection(user_selection):
    if user_selection in options_list or user_selection == 'e':
        return True
    return False
        
def return_menu_function_name(user_selection):
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
            if check_user_selection(user_selection):
                function_name = return_menu_function_name(user_selection)
                call_menu_function(function_name)
                break
            else:
                error = True
            
    else:
        print(messages.end_the_program)

if __name__ == "__main__":
    main()
