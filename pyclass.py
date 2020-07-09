class Rectangular:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def square(self):
        print(f"넓이는 {self.x * self.y}")


    def circumference(self):
        print(f"둘레는 {2*(self.x + self.y)}")


rec1 = Rectangular(3,5)
rec1.square()
rec1.circumference()


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name}, \"bark!! bark!!!\"")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} \"Nya~\"")


dog = Dog('바둑이')
cat = Cat('나비')
dog.speak()
cat.speak()