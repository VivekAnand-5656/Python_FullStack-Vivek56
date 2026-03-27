# ============== Polymorphism (same function, different behavior) =============

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
c = Cat()
c.sound()