import json
# Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

user_str = []
while True:
    new_str = input("Введите строку. Для окончания введите пустую строку >>>")
    if new_str == "":
        break
    else:
        user_str.append(new_str)
        user_str.append("\n")

print(user_str)

with open("my_file.txt", "w+") as my_file:
    my_file.writelines(user_str)
    my_file.seek(0)
    for line in my_file:
        print(line)


# Задание 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("file_for_z2.txt") as my_file:
    my_list = []
    count = 0
    for ind, line in enumerate(my_file):
        print(line)
        count += 1
        my_list.append(line.split(" "))
        length = len(my_list)
        print("В {} строке слов: {}".format(ind + 1, length + 1))
    print("В файле строк: {}".format(count))

# Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад
# менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("file_for_z3.txt") as my_file:
    person = []
    for line in my_file:
        person.append(line.replace('\n', ''))

    print(person)
    total = 0
    count = 0
    for el in person:
        surname, salary = el.split(" ")
        count += 1
        if float(salary) <= 20000:
            print(surname, "имеет зарплату ниже 20000 руб.")
        total = total + float(salary)
    middle_salary = total / count
    print("Средняя зарплата сотрудников составляет {} рублей".format(int(middle_salary)))

# Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

with open("file_for_z4.txt") as my_file:
    my_list = []
    for line in my_file:
        my_list.append(line.replace('\n', ''))
    print(my_list)
    my_list_upd = []
    for el in my_list:
        word, number = el.split(" - ")
        if word == "One":
            word = "Один"
        elif word == "Two":
            word = "Два"
        elif word == "Three":
            word = "Три"
        elif word == "Four":
            word = "Четыре"
        my_list_upd.append(word + " - " + number + "\n")

print(my_list_upd)

with open("file_for_z4_upd.txt", "w+") as my_file_upd:
    my_file_upd.writelines(my_list_upd)
    my_file_upd.seek(0)
    for line in my_file_upd:
        print(line)

# Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("file_for_z5.txt", "w+") as my_file:
    my_file.write(input("Введите числа через пробел >>>"))
    my_file.seek(0)
    my_list = []

    for line in my_file:
        my_list.extend(line.split(" "))
    print(my_list)
    summa = 0
    for el in my_list:
        summa = summa + int(el)
    print("Сумма введенных чисел составляет ", summa)

# Задание 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
# и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

with open("file_for_z6.txt") as my_file:
    lessons = []
    for line in my_file:
        line = line.replace(": ", " ")
        line = line.replace("(л) ", " ")
        line = line.replace("(пр) ", " ")
        line = line.replace("(лаб)", "")
        line = line.replace(" - ", " ")
        line = line.replace(" -", "")
        line = line.replace("\n", "")
        lessons.append(line)
    print(lessons)
    lessons_dict = {}

    for el in lessons:
        lesson, *count = el.split(" ")
        summa = sum(map(lambda x: int(x), count))
        lessons_dict.update({lesson: summa})
    print(lessons_dict)

# Задание 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

with open("file_for_z7.txt") as my_file:
    firms = []
    middle_profit = 0
    for line in my_file:
        name, form, revenue, costs = line.split(" ")
        profit = int(revenue) - int(costs)
        firms.append({name: profit})
        if profit > 0:
            middle_profit = middle_profit + profit

    counter = len(firms)
    middle_profit = middle_profit / counter
    firms.append({'average_profit': int(middle_profit)})
    print(firms)

with open("file_for_z7.json", "w") as write_f:
    json.dump(firms, write_f)




