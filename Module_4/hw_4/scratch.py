class FlatIterator:

    def __init__(self, list_of_list):
        self.l_of_l = list_of_list

    def __iter__(self):
        print('Make the list flat again!')
        # self.flat_list = []
        self.index_1, self.index_2 = 0, 0
        return self

    def __next__(self):

        if self.index_1 == len(self.l_of_l):
            raise StopIteration
        if self.index_2 == len(item_1):
            self.index_2 = 0
            self.index_1 += 1
        self.index_2 += 1
        item_1 = self.l_of_l[self.index_1]
        item_2 = item_1[self.index_2]
        return item_2

        # self.flat_list.extend(self.l_of_l[self.index])

list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
my_iterator = FlatIterator(list_of_lists_1)

for my_item in my_iterator:
    print(my_item)
