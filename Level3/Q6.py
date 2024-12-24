class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird:
    def fly(self):
        return f"{self.name} is Flying!"

class Parrot(Bird, Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def speak(self):
        return f"{self.name} says Hello!"


if __name__ == '__main__':
    dog = Dog("Perro")
    assert dog.speak() == "Perro says Woof!"

    cat = Cat("Gato")
    assert cat.speak() == "Gato says Meow!"

    parrot = Parrot("Rio")
    assert parrot.speak() == "Rio says Hello!"
    assert parrot.fly() == "Rio is Flying!"
