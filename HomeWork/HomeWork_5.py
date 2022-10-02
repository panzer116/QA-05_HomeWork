"""
5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
- как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений
этого атрибута нужно использовать методы get и set
"""


class Car:
    def __init__(self, brand, model, year):
        self.transport = None
        self.brand = brand
        self.model = model
        self.year = year

    # полиформизм
    def transports(self):
        print(f'{self.brand} used for transportation {self.transport}')


class Sedan(Car):
    def __init__(self, brand, model, year, color, transport):
        self.transport = transport
        super().__init__(brand, model, year)
        self.__color = color

    def transports(self):
        print(f'{self.brand} used for transportation {self.transport}')

    def coloration(self):
        print(f'My {self.model} is {self.__color}')

    # инкапсуляция
    def get_color(self):
        print(f'{self.__color} is great for the {self.model}')

    def set_color(self, newcolor):
        self.__color = newcolor


class Truck(Car):
    def __init__(self, brand, model, year, payload, transport):
        self.payload = payload
        self.transport = transport
        super().__init__(brand, model, year)

    def transports(self):
        print(f'{self.brand} used for transportation the {self.transport} weighing up to {self.payload}')


# объект (экземпляр класса)
car1 = Sedan("Kia", "Rio", 2020, "red", "people")
car1.transports()
car1.coloration()
car1.get_color()
car1.set_color('blue')
car1.coloration()

car2 = Truck("KaMaz", "6520", 2018, "20 ton", "cargo")
car2.transports()

""" 
5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий 
"""

'git@github.com:panzer116/QA-05_HomeWork.git'
