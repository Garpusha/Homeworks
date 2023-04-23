def string_cleanup(my_str: str) -> str:
    return ''.join([symbol for symbol in my_str if symbol in '{}[]()'])


def balanced_or_not(my_str: str) -> bool:
    while True:
        any_brackets = True
        if '[]' in my_str:
            my_str = my_str.replace('[]', '')
            any_brackets = False
        if '{}' in my_str:
            my_str = my_str.replace('{}', '')
            any_brackets = False
        if '()' in my_str:
            my_str = my_str.replace('()', '')
            any_brackets = False
        if any_brackets:
            if len(my_str) == 0:
                return True
            else:
                return False


while True:
    my_choice = input("Enter string or empty string to exit: ")
    if not my_choice:
        exit()
    print(balanced_or_not(string_cleanup(my_choice)))
