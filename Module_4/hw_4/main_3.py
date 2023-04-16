class FlatIteratorHard:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iters_stack = [iter(self.list_of_list)]
        return self

    def __next__(self):
        while self.iters_stack:
            try:
                next_item = next(self.iters_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iters_stack.pop()
                #  если не получилось, значит итератор пустой
                continue

            if isinstance(next_item, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iters_stack.append(iter(next_item))

            else:
                return next_item
        raise StopIteration



class FlatIterator:

    def __init__(self, list_of_list):
        # self.l_of_l = list_of_list[::-1]
        self.list_of_list = list_of_list

    def __iter__(self):
        self.l_of_l = [iter(self.list_of_list)]
        return self

    def __next__(self):
        # counter = 0
        # length = len(self.l_of_l)
        #


        for element_ in self.l_of_l:
            if isinstance(element_, list):
              FlatIterator(element_)
            else:
                return element_

list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

my_iterator = FlatIteratorHard(list_of_lists_2)
for element in my_iterator:
    print(element)
