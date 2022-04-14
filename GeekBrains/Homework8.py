# Задание 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    def __init__(self, date_str):
        self.str_to_number(date_str)

    @classmethod
    def str_to_number(cls, date_str):
        day, month, year = map(lambda x: int(x), date_str.split("-"))
        print(f'День: {day}, месяц: {month}, год: {year}')
        return [day, month, year]

    @staticmethod
    def date_validation(date):
        day, month, year = Date.str_to_number(date)
        if day > 31:
            print("Номер дня не может превышать 31!")
        elif day <= 0:
            print("Номер дня не может быть равным 0 или иметь отрицательное значение")
        elif month > 12 or month <= 0:
            print("Номер месяца должен принимать значение от 1 до 12!")


my_date = Date(input("Введите дату в формате ДД-ММ-ГГГГ >>>"))
Date.date_validation("25-12-1992")
Date.date_validation("32-12-1992")
Date.date_validation("12-13-1992")


# Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем ноля в
# качестве делителя, программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

class ZeroDivisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(divisible, divider):
    return divisible / divider


param1 = float(input("Введите делимое >>>"))
param2 = float(input("Введите делитель >>>"))

try:
    if param2 == 0:
        raise ZeroDivisionException("На 0 делить нельзя!")
    quotient = division(param1, param2)
    print(f'Результат деления: {quotient}')
except ZeroDivisionException as ex:
    print(ex)


# Задание 3. Создайте собственный класс-исключение, который должен проверять содержимое списка наналичие
# только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя
# данные и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами
# выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе
# пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только
# если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class TypeException(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    element = input("Введите число. Для отмены введите stop >>>")
    try:
        if element == "stop":
            print(my_list)
            break
        element = int(element)
        my_list.append(element)

    except ValueError:
        try:
            raise TypeException("Введено не число. Введите число или stop для отмены>>>")
        except TypeException as te:
            print(te)


# Задания 4-6.
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В
# классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Warehouse:
    def __init__(self, quantity):
        self.quantity = quantity
        self.equipment = []

    def reception(self, equipment: list):
        try:
            if len(self.equipment) >= self.quantity:
                raise CapacityException(len(self.equipment), len(self.equipment) + len(equipment))
            elif len(equipment) > (self.quantity - len(self.equipment)):
                raise CapacityException(self.quantity, len(self.equipment) + len(equipment))
        except CapacityException as ex:
            print(ex)

        self.equipment.extend(equipment)

    def show(self):
        for el in self.equipment:
            print(f'На складе: {el.__class__.__name__}, стоимость: {el.cost}')


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"На складе не хватает места, вместимость = {self.current} единиц, нужно = {self.needle}"


class Office_Equipment:
    def __init__(self, cost, resource):
        self.cost = cost
        self.resource = resource


class Printer(Office_Equipment):
    def __init__(self, cost, resource, type_eq):
        super().__init__(cost, resource)
        self.type_eq = type_eq


class Scanner(Office_Equipment):
    def __init__(self, cost, resource, auto_feed):
        super().__init__(cost, resource)
        self.auto_feed = auto_feed


class Xerox(Office_Equipment):
    def __init__(self, cost, resource, is_multifunctional):
        super().__init__(cost, resource)
        self.is_multifunctional = is_multifunctional


printer1 = Printer(4000, 10000, "laser")
printer2 = Printer(15000, 100000, "laser")
scanner1 = Scanner(2000, 25000, False)
scanner2 = Scanner(5000, 25000, True)
xerox1 = Xerox(50000, 250000, True)
xerox2 = Xerox(55000, 250000, True)

warehouse = Warehouse(5)
warehouse.reception([printer1, printer2, scanner1])
warehouse.reception([scanner2, xerox1])
warehouse.show()

warehouse.reception([xerox2])


# Задание 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте
# корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма чисел complex1 и complex2: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение чисел complex1 и complex2: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'Комплексное число: {self.a} + {self.b} * i'


complex1 = ComplexNumber(5, 4)
complex2 = ComplexNumber(6, -2)
print(complex1)
print(complex2)
print(complex1 + complex2)
print(complex1 * complex2)

