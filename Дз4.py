class Car:
    def __init__(self, model):
        self.model = model
        self.engine_on = False
        self.mileage = 0
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{self.model}: Двигун заведено.")
        else:
            print(f"{self.model}: Двигун вже працює.")
    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print(f"{self.model}: Двигун вимкнено.")
        else:
            print(f"{self.model}: Двигун вимкнено.")
    def drive(self, distance):
        if self.engine_on:
            self.mileage += distance
            print(f"{self.model}: Проїхав {distance} км. Загальний пробіг: {self.mileage} км.")
        else:
            print(f"{self.model}: Двигун вимкнено, їхати не можна ")
class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car
    def start_trip(self, distance):
        print(f"{self.name} вирішив поїхати")
        self.car.start_engine()
        self.car.drive(distance)
    def end_trip(self):
        print(f"{self.name} закінчив поїздку")
        self.car.stop_engine()
my_car = Car("Toyota")
driver = Driver("Вася", my_car)
driver.start_trip(50)
driver.end_trip()
my_car.drive(30)
