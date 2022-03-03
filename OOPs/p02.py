class Animal:
    def __init__(self, name):
        self.name = name

    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Animal"

class Wild(Animal):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Wild. {}".format(Animal.get_the_info(self))

class Pet(Animal):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Pet. {}".format(Animal.get_the_info(self))

class Canine(Animal):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Canine. {}".format(Animal.get_the_info(self))

class Leopard(Wild):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Leopard. {}".format(Wild.get_the_info(self))

class Tiger(Wild):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Tiger. {}".format(Wild.get_the_info(self))

class Dog(Pet):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Dog. {}".format(Pet.get_the_info(self))

class Fox(Canine):
    def get_the_name(self):
        return "I am " + self.name

    def get_the_info(self):
        return "I am Fox. {}".format(Canine.get_the_info(self))

# print(Animal.get_name('leo'))
animal = Tiger("Leo")
print(animal.get_the_name())
print(animal.get_the_info())