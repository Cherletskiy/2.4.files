import pprint

def get_dict(recipes: str) -> dict:
    """
    Функция принимает на вход путь до файла с рецептами, читает построчно и формируеет словарь с рецептами.
    :param recipes: путь до файла
    :return: словарь вида:
    {
    'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    }
    """
    dict_rep = {}
    with open(recipes, "r", encoding="utf-8") as f:
        while True:
            name = f.readline().strip()
            if name == "":
                break
            count = int(f.readline().strip())
            dict_rep[name] = []
            for i in range(count):
                ing, count, unit = f.readline().strip().split(" | ")
                dict_rep[name].append({"ingredient_name": ing, "quantity": count, "measure": unit})
            f.readline()
    return dict_rep


cook_book = get_dict('recipes.txt')
# print(cook_book)
# pprint.pprint(cook_book)

