


from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
   @abstractmethod
   def do_something(self):
       pass

class AnotherSubclass(AbstractClassExample):
   def do_something(self):
       super().do_something()
       print("The subclass is doing something")

x = AnotherSubclass()
x.do_something() # Output: The subclass is doing something
#encapsulation


# This principle involves bundling data and methods that operate on that data into a single unit, a class. It restricts direct access to some of an object's components. In Python, we can achieve encapsulation by declaring the class variables as private using underscore (_variable) or double underscore (__variable). However, Python doesn't strictly enforce privacy, it merely suggests it.

class Car:
   _brand = None # Private variable

   def set_brand(self, brand):
       self._brand = brand

   def get_brand(self):
       return self._brand

car = Car()
car.set_brand("Toyota")
print(car.get_brand()) # Output: Toyota




# Inheritance: This principle allows one class to inherit the characteristics and behaviors of another class. The class being inherited from is known as the superclass, and the class doing the inheriting is known as the subclass.

class Vehicle:
   def move(self):
       print("Vehicles can move")

class Car(Vehicle):
   def honk(self):
       print("Car honks")

my_car = Car()
my_car.move() # Output: Vehicles can move
my_car.honk() # Output: Car honks


#Polymorphism: This principle allows objects of different types to be treated as instances of a common superclass. In Python, polymorphism is achieved by defining methods in the subclasses that have the same name as those defined in the superclass.

class Bird:
   def fly(self):
       print("I can fly")

class Duck(Bird):
   def swim(self):
       print("I can swim")

duck = Duck()
duck.fly() # Output: I can fly
duck.swim() # Output: I can swim



# Abstraction: This principle involves hiding the complexity of a system and exposing only the essential features to the users. In Python, abstraction is achieved by creating abstract classes and methods. An abstract class is a class that cannot be instantiated and is meant to be subclassed by other classes. Abstract methods, declared in an abstract class, don't contain any implementation and must be implemented in any non-abstract child class.




# class Barista:
#     def __init__(self,name):
#         self.name = name
#         self.cafe = CoffeeM("Cafe")
#     def make_coffee(self, beans):
#         self.cafe.brew_now(beans)