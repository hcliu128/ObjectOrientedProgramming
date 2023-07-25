import abc 

class Animal(abc.ABC):
    @abc.abstractmethod
    def sound(self):
        return NotImplemented
    def eat(self):
        print(f"{self.name} is eating...")
    def sit(self):
        print(f"{self.name} is sitting...")
    def sleep(self):
        print(f"{self.name} is sleeping...")
    
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} is barking...")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} is meowing...")

Bob = Dog("Bob")
Billy = Cat("Billy")
Bob.sound()
Bob.eat()
Billy.sound()
Billy.sit()
print(isinstance(Bob, Animal) and issubclass(Dog, Animal))
print(isinstance(Billy, Animal) and issubclass(Cat, Animal))
