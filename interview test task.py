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


class KS():
    def weight(self):
        self.weight = randint(5, 15)
        return self.weight

    def color(self):
        color_list = [
            'White', 'Black', 'Brown',
            'Blue', 'Gray', 'Red', 'Orange',
            'Yellow', 'Purple', 'Pink']
        self.color = color_list[randint(0, 9)]
        return self.color


class Bicycle(KS):
    def __init__(self):
        self.transmission = randint(1, 20)
        self.color = KS().color()


class EKS(KS):
    def __init__(self):
        self.weight = KS().weight()
        self.power = randint(180, 480)
        self.color = KS().color()

Samo = KS()
print(Samo.color(), Samo.weight())
Yamaha = EKS()
print(Yamaha.power, Yamaha.color)