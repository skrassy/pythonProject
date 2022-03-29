from time import sleep


# Задание 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        for color in self.__color:
            print(f"Горит {color} свет")
            if color == "Красный":
                sleep(7)
            elif color == "Желтый":
                sleep(2)
            elif color == "Зеленый":
                sleep(5)


traffic_light = TrafficLight()
traffic_light.running()


# Задание 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании
# экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.

class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self):
        mass_sqr_m = float(input("Введите массу в кг дорожного полотна площадью 1 кв.м и толщиной 1 см >>>"))
        thickness = float(input("Введите толщину дорожного полотна в см >>>"))
        mass = self._width * self._length * mass_sqr_m * thickness
        print(f"Масса дорожного полотна составляет {mass} тонн")


road_1 = Road(50, 10)
road_1.mass_calculation()


# Задание 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _salary = {}

    def __init__(self, surname, name, position, wage, bonus):
        self.surname = surname
        self.name = name
        self.position = position
        self._salary = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, surname, name, position, wage, bonus):
        super().__init__(surname, name, position, wage, bonus)

    def get_full_name(self):
        print(f"Фамилия и имя сотрудника: {self.surname} {self.name}")

    def get_total_income(self):
        total_income = 0
        for k, v in self._salary.items():
            total_income = total_income + v
        print(f"Зарплата с учетом премии составляет {total_income} рублей")


worker_1 = Position("Петров", "Игорь", "менеджер", 20000, 5000)
worker_2 = Position("Иванов", "Александр", "старший менеджер", 50000, 15000)
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()


# Задание 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые
# должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.name} составляет {self.speed} км/ч")

    def info(self):
        print(f"Марка автомобиля: {self.name}, "
              f"Цвет: {self.color}, "
              f"Скорость: {self.speed} км/ч, "
              f"Является полицейской: {self.is_police}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Превышение скорости! Скорость не должна превышать 60 км/ч!")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Превышение скорости! Скорость не должна превышать 40 км/ч!")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(55, "red", "Mazda", False)
car_1.info()
car_1.go()
car_1.show_speed()
car_1.turn("направо")
car_1.stop()

car_2 = TownCar(85, "black", "Skoda", False)
car_2.info()
car_2.go()
car_2.show_speed()
car_2.turn("направо")
car_2.stop()

car_3 = WorkCar(45, "blue", "JohnDeer", False)
car_3.info()
car_3.go()
car_3.show_speed()
car_3.turn("налево")
car_3.stop()


# Задание 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title, color):
        self.title = title
        self.color = color

    def draw(self):
        print(f"Запуск отрисовки. След оставляет {self.title}")


class Pen(Stationery):

    def __init__(self, title, color):
        super().__init__(title, color)

    def draw(self):
        super().draw()
        print(f"Эта ручка имеет {self.color} цвет")


class Pencil(Stationery):

    def __init__(self, title, color):
        super().__init__(title, color)

    def draw(self):
        super().draw()
        print(f"Этот карандаш имеет {self.color} цвет")


class Handle(Stationery):

    def __init__(self, title, color):
        super().__init__(title, color)

    def draw(self):
        super().draw()
        print(f"Этот маркер имеет {self.color} цвет")


stationery = Stationery("Письменная принадлежность", "неизвестно")
pen = Pen("Ручка", "синий")
pencil = Pencil("Карандаш", "красный")
handle = Handle("Маркер", "зелёный")

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()

