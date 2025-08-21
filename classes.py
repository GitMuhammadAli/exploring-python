# ---- 1. Basic Class ----
class Person:
    # Class attribute (shared by all instances)
    species = "Human"

    # Constructor
    def __init__(self, name, age):
        self.name = name        # Instance attribute
        self.age = age

    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


# ---- 2. Creating Objects ----
p1 = Person("Ali", 25)
p2 = Person("Sara", 30)

print(p1.greet())   # "Hello, my name is Ali and I'm 25 years old."
print(Person.species)  # Accessing class attribute


# ---- 3. Class Methods ----
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


Student.change_school("XYZ School")
print(Student.school)


# ---- 4. Static Methods ----
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


print(MathUtils.add(5, 3))


# ---- 5. Inheritance ----
class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Woof!"

c = Animal()
d = Dog()
print(d.sound())   # "Woof!"
print(c.sound())   


# ---- 6. super() ----
class Parent:
    def show(self):
        return "I am the parent"


class Child(Parent):
    def show(self):
        parent_message = super().show()
        return parent_message + " and I am the child"


print(Child().show())


# ---- 7. Encapsulation (Private Members) ----
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())  # 150


# ---- 8. Polymorphism ----
class Cat:
    def speak(self):
        return "Meow"


class Dog:
    def speak(self):
        return "Woof"


for animal in (Cat(), Dog()):
    print(animal.speak())


# ---- 9. Magic / Dunder Methods ----
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book("Python 101", 200)
b2 = Book("Advanced Python", 300)
print(str(b1))          # Book: Python 101, Pages: 200
print(len(b1))          # 200
print(b1 + b2)          # 500


# ---- 10. Abstract Classes ----
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


print(Circle(5).area())


# ---- 11. Dataclasses (Python 3.7+) ----
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


p = Point(10, 20)
print(p)   # Point(x=10, y=20)



class Person :
    def __init__(self , name):
        self.name = name 

    def talk(self):

        print(f"hi i am {self.name}")


p = Person("Ali")
p.talk()