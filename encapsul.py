class Car:
    def __init__(self, name, model):
        self.name = name
        self._model = model
    def info(self):
        print(f'Car name: {self.name} | model: {self._model}')   
        
my_car = Car("Toyota", "Camrito")
print(my_car.name)
# print(my_car.model) # this is not accessible here 
print(my_car._model)
my_car.info()