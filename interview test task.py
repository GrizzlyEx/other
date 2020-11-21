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
Электросамокат 'Electric Scooter' (ES) - вес, цвет, мощность электромотора.
Мотоцикл 'Motorcycle' (Moto) – вес, цвет, мощность мотора, время разгона до 100 км/ч.
Автомобиль 'Car' – вес, цвет, мощность мотора, время разгона до 100 км/ч,
                                        расположение руля(правое/левое).
"""

from random import randint


class Garage:
    def color(self):
        color_list = [
            'White', 'Black', 'Brown',
            'Blue', 'Gray', 'Red', 'Orange',
            'Yellow', 'Purple', 'Pink']
        return color_list[randint(0, 9)]

    def racing_100(self, a):
        return randint(100//a, 150//a)/10

    def rudder(self):
        rudder = ['Right-hand', 'Left-hand']
        return rudder[randint(0, 1)]


class KS(Garage):
    def __init__(self):
        self.weight = randint(2, 10)
        self.color = Garage().color()
        print(f'''Kick Scooter:
    weight - {self.weight}kg,
    color - {self.color}''')
        print('-'*28)


class Bicycle(Garage):
    def __init__(self):
        self.weight = randint(10, 20)
        self.color = Garage().color()
        self.transmission = randint(1, 15)
        print(f'''Bicycle:
    weight - {self.weight}kg,
    color - {self.color},
    number of gears - {self.transmission}''')
        print('-' * 28)


class ES(Garage):
    def __init__(self):
        self.weight = randint(10, 30)
        self.color = Garage().color()
        self.power = randint(180, 500)  # Watt
        print(f'''Electric Scooter:
    weight - {self.weight}kg,
    color - {self.color},
    power of engine - {self.power}Wt''')
        print('-' * 28)


class Moto(Garage):
    def __init__(self):
        self.weight = randint(110, 330)
        self.color = Garage().color()
        self.power = randint(20, 100)
        self.racing_100 = Garage().racing_100(self.power//20)
        print(f'''Motorcycle:
    weight - {self.weight}kg,
    color - {self.color},
    power of engine - {self.power}hp,
    racing to 100km/h - {self.racing_100}sec''')
        print('-' * 28)


class Car(Garage):
    def __init__(self):
        self.weight = randint(1000, 2500)
        self.color = Garage().color()
        self.power = randint(100, 280)
        self.racing_100 = Garage().racing_100(self.power//70)
        self.rudder = Garage().rudder()
        print(f'''Car:
    weight - {self.weight}kg,
    color - {self.color},
    power of engine - {self.power}hp,
    racing to 100km/h - {self.racing_100}sec,
    steering side - {self.rudder}''')
        print('-' * 28)


garage = ['Kick Scooter', 'Bicycle',
          'Electric Scooter', 'Motorcycle', 'Car']
garage_qua = []

for i in range(len(garage)):
    garage_qua.append(randint(0, 2))
    for k in range(garage_qua[i]):
        if garage[i] == 'Kick Scooter':
            KS()
        elif garage[i] == 'Bicycle':
            Bicycle()
        elif garage[i] == 'Electric Scooter':
            ES()
        elif garage[i] == 'Motorcycle':
            Moto()
        else:
            Car()


print(f'Total transport in the garage: {sum(garage_qua)}')


