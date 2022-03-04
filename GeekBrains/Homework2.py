# Задание 1
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
# для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно,
# в программе.

my_list = [123, "word", 256.7, 567, "qwerty", None, 15]
print(my_list)
for el in my_list:
    print(type(el))

# Задание 2
# Для списка реализовать обмен значений соседних элементов, т.е.
# значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = input("Введите элементы списка через пробел").split(' ')
print(my_list)
for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)


# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через list

season = ["winter", "spring", "summer", "autumn"]
month = int(input("Введите месяц в виде целого числа от 1 до 12 >>>"))
if 3 < month <= 12:
    print(season[0])
elif 3 <= month <= 5:
    print(season[1])
elif 6 <= month <= 8:
    print(season[2])
elif 9 <= month <= 11:
    print(season[3])
else:
    print("Вы ввели некорректный номер месяца")

# Решение через dict

season_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring",
               5: "spring", 6: "summer", 7: "summer", 8: "summer",
               9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
month = int(input("Введите месяц в виде целого числа от 1 до 12 >>>"))
for el in season_dict.keys():
    if el == month:
        print(season_dict.get(el))


# Задание 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

phrase = input("Введите фразу >>>").split(' ')
for ind, el in enumerate(phrase):
    print(ind, el[:10])

# Задание 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
while True:
    number = input("Введите целое положительное число. Для выхода введите exit >>>")
    if number == "exit":
        break
    number = abs(int(number))
    for ind, el in enumerate(my_list):
        if el < number:
            my_list.insert(ind, number)
            break
        if ind >= len(my_list) - 1:
            my_list.append(number)
            break

    print(my_list)
print("Программа завершена")

# Задание 6
# *Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

my_list = []
name_list = []
price_list = []
quantity_list = []
index = 0
my_dict = {}
while True:
    next_el = input("Хотите ввести товарную позицию? Нажмите Y для продолжения или N для выхода").upper()
    if next_el == "N":
        break

    name = input("Введите название товара >>>")
    name_list.append(name)
    price = int(input("Введите цену товара >>>"))
    price_list.append(price)
    quantity = int(input("Введите количество штук товара >>>"))
    quantity_list.append(quantity)
    product = {"Название": name, "Цена": price, "Количество": quantity}
    print(product)
    my_list.append((index, product))
    index += 1
    print(my_list)

name_dict = {"Название": name_list}
price_dict = {"Цена": price_list}
quantity_dict = {"Количество": quantity_list}
my_dict.update(name_dict)
my_dict.update(price_dict)
my_dict.update(quantity_dict)
print(my_dict)

