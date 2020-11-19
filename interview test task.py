"""
Необходимо реализовать алгоритм с применением принципов ООП.
При запуске алгоритм генерирует ‘гараж’, в котором находятся
транспортные средства следующих типов: самокат, велосипед,
электросамокат, мотоцикл, автомобиль (от 0 до 2 единиц каждого из типов).
У каждого из транспортных средств есть набор свойств, который
генерируется при создании. Затем алгоритм выводит общее количество транспортных
средств в гараже и количество автомобилей, а также подробное описание каждого
из транспортных средств (Например ‘Самокат: вес - 12.4 кг, цвет – красный’).

Свойства транспортных средств:
Самокат 'Kick scooter' (KS) – вес, цвет.
Велосипед 'Bicycle' – вес, цвет, количество передач.
Электросамокат 'EKS' - вес, цвет, мощность электромотора.
Мотоцикл 'Motorcycle' (Moto) – вес, цвет, мощность мотора, время разгона до 100 км/ч.
Автомобиль 'Car' – вес, цвет, мощность мотора, время разгона до 100 км/ч,
                                        расположение руля(правое/левое).
"""

from random import randint


class Garage():
    def weight(self, a, b):
        return randint(a, b)

    def color(self):
        color_list = [
            'White', 'Black', 'Brown',
            'Blue', 'Gray', 'Red', 'Orange',
            'Yellow', 'Purple', 'Pink']
        self.color = color_list[randint(0, 9)]
        return self.color

    def transmission(self, a=1, b=15):
        return randint(a, b)

    def power(self, a, b):
        return randint(a, b)

    def racing_100(self, a):
        return randint(100//a, 150//a)/10

    def rudder(self):
        rudder = ['Right-hand', 'Left-hand']
        return rudder[randint(0, 1)]


class KS(Garage):
    def __init__(self):
        self.weight = Garage().weight(2, 10)
        self.color = Garage().color()


class Bicycle(Garage):
    def __init__(self):
        self.weight = Garage().weight(10, 20)
        self.color = Garage().color()
        self.transmission = Garage().transmission()


class EKS(Garage):
    def __init__(self):
        self.weight = Garage().weight(10, 30)
        self.color = Garage().color()
        self.power = Garage().power(180, 500)  # Watt


class Moto(Garage):
    def __init__(self):
        self.weight = Garage().weight(110, 330)
        self.color = Garage().color()
        self.power = Garage().power(20, 100)
        self.racing_100 = Garage().racing_100(self.power//20)


class Car(Garage):
    def __init__(self):
        self.weight = Garage().weight(1000, 2500)
        self.color = Garage().color()
        self.power = Garage().power(100, 280)
        self.racing_100 = Garage().racing_100(self.power//70)
        self.rudder = Garage().rudder()


garage = ['KS', 'Bicycle',
          'EKS', 'Moto', 'Car']
garage_qua = []
for i in range(len(garage)):
    garage_qua.append(randint(0, 2))
    for k in range(garage_qua[i]):
        print(garage[i])

print(garage_qua)


