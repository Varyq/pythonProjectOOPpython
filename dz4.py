class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100

    def play(self):

        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} грається Енергія: {self.energy}")
        else:
            print(f"{self.name} втомлений, щоб гратися.")

    def eat(self):

        self.energy += 30
        print(f"{self.name} поїв Енергія: {self.energy}")


my_pet = Pet("Рижик", "кіт")


my_pet.play()
my_pet.eat()
my_pet.play()

