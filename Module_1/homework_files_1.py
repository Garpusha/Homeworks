def get_shop_list_by_dishes(dishes, person_count, c_book):
    need_to_buy = {}
    ingredients = []
    [[ingredients.append(item) for item in c_book[dish]] for dish in dishes]
    for my_ing in ingredients:
        if need_to_buy.get(my_ing['ingredient_name']) == None:
            need_to_buy[my_ing['ingredient_name']] = {'measure': my_ing['measure'],
                                                      'quantity': int(my_ing['quantity']) * person_count}
        else:
            (need_to_buy[my_ing['ingredient_name']]['quantity']) += int(my_ing['quantity']) * person_count
    return need_to_buy


recipes = open('files_Task_1\\recipes.txt', 'r', encoding='utf-8')
cook_book = {}
line = recipes.readline()
while line != '':
    dish_name = line.rstrip()
    cook_book[dish_name] = []
    items = int(recipes.readline().rstrip())
    for index in range(items):
        ingredient, quantity, measure = recipes.readline().rstrip().split(' | ')
        cook_book[dish_name].append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})
    line = recipes.readline()
    line = recipes.readline()
recipes.close()
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book))
