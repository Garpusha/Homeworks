class Stack:

    def __init__(self):
        self.stack_array = []

    def is_empty(self) -> bool:
        return len(self.stack_array) == 0

    def push(self, incoming):
        self.stack_array.append(incoming)

    def pop(self):
        if len(self.stack_array) != 0:
            return self.stack_array.pop()
        else:
            return

    def peek(self):
        return self.stack_array[-1]

    def size(self) -> int:
        return len(self.stack_array)

    def content(self) -> list:
        return self.stack_array


def get_choice() -> str:
    print('''
    1. Is the stack empty?
    2. Add element
    3. Return last element and remove
    4. Return last element
    5. Print length of the stack
    6. Print stack content
    0. Exit\n''')
    return input('Enter option: ')


if __name__ == '__main__':
    my_stack = Stack()

    while True:
        match get_choice():
            case '1':
                print(f'{my_stack.is_empty()}\n')
            case '2':
                my_stack.push(input('Enter new element: '))
            case '3':
                print(f'Last element is: {my_stack.pop()}')
            case '4':
                print(f'Last element is: {my_stack.peek()}')
            case '5':
                print(f'Total elements: {my_stack.size()}')
            case '6':
                print(f'Here is the stack: {my_stack.content()}')
            case '0':
                exit()
