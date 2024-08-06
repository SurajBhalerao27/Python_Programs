from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Woof!'

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Meow!'

cat = Cat("Dolly")
dog = Dog("Rocky")
print(f'{cat.name} says: {cat.make_sound()}')
print(f'{dog.name} says: {dog.make_sound()}')