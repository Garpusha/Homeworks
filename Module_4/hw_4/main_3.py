class FlatIterator:

    def __init__(self, list_of_list):
        self.l_of_l = list_of_list[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if not self.l_of_l:
                raise StopIteration
            element_ = self.l_of_l.pop()
            if isinstance(element_, list):
                itr = FlatIterator(element_)
                return next(itr)
            else:
                return element_


list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

my_iterator = FlatIterator(list_of_lists_2)
for element in my_iterator:
    print(element)
