# Нужно написать класс дом с подъездами и этажами,
# на каждом этаже по 4 квартиры.
# Нужно вывести сколько квартир находится в указанном доме,
# создать несколько экземпляров и сравнить их
# Далее нужно посчитать сколько квартир находится в районе
# (к примеру вы создали 10 экземпляров) и нужно узнать сколько всего квартир

class House:
    counter = 0
    def __init__(self, name, entrance, floor):
        self.name = name
        self.entrance = entrance
        self.floor = floor
        House.counter += 1

    def __str__(self):
        return '{}: количество этажей - {}, количество подъездов - {}'.format(
            self.name, self.entrance, self.floor)

    def home_apartment_counting(self):
        self.numberofapartments=self.entrance*self.floor*4
        print(f'Количество квартир: {self.numberofapartments}')


house1 = House('House №1', 2,4)
print(house1)
house1.home_apartment_counting()
print()
house2 = House('House №2', 3,5)
print(house2)
house2.home_apartment_counting()
print()
house3 = House('House №3', 5,6)
print(house3)
house3.home_apartment_counting()
print()
house4 = House('House №4', 1,8)
print(house4)
house4.home_apartment_counting()
print()
print(f'Количество домов в районе: {House.counter}')






