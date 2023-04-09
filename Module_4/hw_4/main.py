class FlatIterator:

    def __init__(self, list_of_list):
        self.l_of_l = list_of_list


    def __iter__(self):
        print('Make the list flat again!')
        self.flat_list = []
        self.index = 0
        return self

    def __next__(self):

        if self.index == len(self.l_of_l):
            raise StopIteration
        # self.flat_list.extend(self.l_of_l[self.index])
        self.flat_list.extend(self.l_of_l[self.index])
        self.index += 1
        return self.flat_list

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
