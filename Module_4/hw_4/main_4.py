def flat_generator_v5(list_of_list):
    for i in list_of_list:
        if isinstance(i, list):
            for j in flat_generator_v5(i):
                yield j
        else:
            yield i


def test_task_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for IteratorClass in (FlatIteratorV1, FlatIteratorV2, FlatIteratorV3, FlatIteratorV4):

        for flat_iterator_item, check_item in zip(
                IteratorClass(list_of_lists_1),
                ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ):
            assert flat_iterator_item == check_item

        assert list(IteratorClass(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_task_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for yield_function in (flat_generator_v1, flat_generator_v2, flat_generator_v3, flat_generator_v4):

        for flat_iterator_item, check_item in zip(
                yield_function(list_of_lists_1),
                ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ):
            assert flat_iterator_item == check_item

        assert list(yield_function(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

        assert isinstance(yield_function(list_of_lists_1), types.GeneratorType)


def test_task_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIteratorHard(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIteratorHard(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


def test_task_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_v5(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_v5(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_v5(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':

    test_task_1()
    test_task_2()
    test_task_3()
    test_task_4()