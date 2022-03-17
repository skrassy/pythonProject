import itertools
from collections import Counter
from functools import reduce
from itertools import count, cycle
from math import factorial

# Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

# Решение во втором файле с названием Homework4_z1


# Задание 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

# По непонятной причине импорт функции pairwise работает некорректно,
# поэтому прописываю функцию вручную

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [b for a, b in pairwise(example_list) if a < b]
print(new_list)

# Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.


my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# Задание 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]


first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_dict = dict(Counter(first_list))
print(my_dict)
second_list = [k for k, v in my_dict.items() if v == 1]
print(second_list)


# Задание 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.


def my_func(prev_el, el):
    return prev_el * el


my_list_2 = [el for el in range(100, 1001) if el % 2 == 0]

print(my_list_2)
print(reduce(my_func, my_list_2))

# Задание 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


for el in count(3):
    if el >= 11:
        break
    else:
        print(el)

original_list = [el for el in range(1, 7)]
counter = 0
for el in cycle(original_list):
    if counter > 15:
        break
    else:
        print(el)
        counter += 1


# Задание 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за
# получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.


def fact(n):
    for el in range(n):
        yield factorial(el)


for elem in fact(5):
    print(elem)