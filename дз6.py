class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"{self.name} видає звук")
class Flyable:
    def fly(self):
        print(f"{self.name} летить")
class Swimmable:
    def swim(self):
        print(f"{self.name} плаває у воді")
class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} крякає")
donald = Duck("Дональд")
donald.make_sound()
donald.fly()
donald.swim()
