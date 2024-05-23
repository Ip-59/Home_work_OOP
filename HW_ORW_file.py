# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»
# Необходимо написать программу для кулинарной книги.


# Задача №1
# Должен получится следующий словарь cook_book

import os
file_path = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = {}
recipe = []
ingredient = {}
all_ingredients =[]

with open(file_path) as f:
    for line in f:
        if len(line.rstrip("\n")) > 0:
            name_dish = line.rstrip("\n")
            number_ingredients = int(f.readline().rstrip("\n"))
            recipe = []
            for i in range(number_ingredients):
                tmp_str = f.readline().rstrip("\n")
                tmp_list = tmp_str.split(' | ')
                ingredient = {"name_ingredient":tmp_list[0], "quantity":tmp_list[1], "unit_measurement":tmp_list[2]}
                recipe.append(ingredient)
        else:
            continue
        cook_book[name_dish] = recipe


# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

dishes = ['Фахитос', 'Омлет']
number_of_persons = 2

def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients =[]
    shop_list = {}
    for dish in dishes:
        all_ingredients.extend(cook_book[dish])
    for ingredient in all_ingredients:
        shop_list_key = ingredient['name_ingredient']
        if shop_list.get(shop_list_key) == None:
            shop_list_value = {'measure': ingredient['unit_measurement'], 'quantity': int(ingredient['quantity'])*person_count}
            shop_list.setdefault(shop_list_key, shop_list_value)
        else:
            shop_list[shop_list_key] ['quantity'] += int(ingredient['quantity'])*person_count
    return shop_list


shop_list_by_dishes = get_shop_list_by_dishes(dishes, number_of_persons)
# print(shop_list_by_dishes)


# Задача №3
# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны/
# Необходимо объединить их в один по следующим правилам:
# 1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# 2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

file = []
len_file = []
for i in range(3):
    file.append([])
    file_name = str(i+1)+'.txt'
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path) as f:
        file[i].append(file_name)
        file[i].append(0)
        file[i].append(f.readlines())
        len_file.append(len(file[i][2]))
        file[i][1] = len_file[i]

file_path = os.path.join(os.getcwd(), 'Итоговый файл.txt')

with open(file_path, 'a') as fa:
    for i in sorted(len_file):
        number_file = len_file.index(i)
        string_for_write = file[number_file][0] +'\n' + str(file[number_file][1])+'\n' + str(''.join(file[number_file][2])) + '\n'
        fa.write(string_for_write)


