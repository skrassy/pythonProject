# Задание 1
a = 12
b = 34
c = a + b
print("a + b = ", c)
x = 99
c = x % a
print(c)
print("a > b = ", a > b)

name = input("Введите имя >>> ")
age = int(input("Введите возраст >>> "))
print("Привет, {}! Твой возраст составляет {} лет!".format(name, age))

login = input("Введите имя пользователя >>> ")
password = input("Введите пароль >>> ")
print("Привет, {}! Благодарим за регистрацию!".format(login))

# Задание 2
time = int(input("Введите время в секундах >>> "))
hour = time // 3600
minutes = (time % 3600) // 60
seconds = time - (hour * 3600) - (minutes * 60)
print("Введенное время составляет {} часов {} минут {} секунд".format(hour, minutes, seconds))

# Задание 3
n = int(input("Введите целое число n >>> "))
nn = n * 11
nnn = n * 111
summa = n + nn + nnn
print("n + nn + nnn = ", summa)

# Задание 4
number = int(input("Введите целое положительное число >>> "))
max_num = number % 10
while number >= 10:
    number = number // 10
    if number % 10 > max_num:
        max_num = number % 10
print("Наибольшая цифра в числе - ", max_num)

# Задание 5
revenue = int(input("Введите значение выручки компании >>>"))
costs = int(input("Введите значение издержек компании >>>"))
if revenue > costs:
    profit = revenue - costs
    print("Компания получила прибыль в размере ", profit)
    profitability = profit / revenue
    print("Рентабельность компании составила ", profitability)
    quantity = int(input("Введите количество сотрудников в компании >>>"))
    profit_per_employee = profit / quantity
    print("Прибыль в расчете на 1 сотрудника составила ", profit_per_employee)
elif revenue == costs:
    print("Компания не получила прибыли")
else:
    print("Компания работает в убыток!")

# Задание 6
a = int(input("Введите расстояние в км, которое пробежал спортсмен в 1й день >>>"))
b = int(input("Введите расстояние, которое должен пробегать спортсмен >>>"))
count = 1
while a < b:
    a = a + (0.1 * a)
    count += 1
print("На {} день тренировок спортсмен будет пробегать {} километров".format(count, b))
