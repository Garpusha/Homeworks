def task_1(source_data):
    source_data = [i for i in reversed(source_data) if "Россия" in list(i.values())[0]]
    return len(source_data)


def task_2(source_data):
    result = []
    [result.extend(i) for i in source_data.values()]
    return set(result)


def task_3(source_data):
    d = dict()
    items = len(source_data)
    i = [len(i.split()) for i in source_data]
    s = set(i)
    for n in s:
        d[n] = round(i.count(n) / items * 100, 2)
    return d
