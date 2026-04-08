#recursive 
def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)
n=5
print(sum(n))
#factorial
def fac(n):
    if n == 0:
        return 1
    return n+fac(n-1)
print(fac(6))
#fibanacci
def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))
#range function for two iterations
for i in range(0,10,2):
    print(i)
#range function decrase by 2
for i in range(10,0,-2):
    print(i)
#iterators
s="Lokesh"
myit=iter(s)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#inheritence

class Employee:
    def show_details(self):
        print("This is Employee class method")

class Developer(Employee):
    def dev_work(self):
        print("This is Developer class method")

dev = Developer()

dev.dev_work()


dev.show_details()
#polymorphism
class Bird:         
    def intro(self): 
        print("There are many types of birds.") 
    def flight(self): 
        print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
#Single Inheritance 
class Animal:
    def eat(self):
        print("animal Eating")
class Dog(Animal):
    def bark(self):
        print("Dog Barking")
d=Dog()
d.eat()
d.bark()
#2.person class 
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
p1=Person("Lokesh",22)
p1.display()
#1.Multiple Inheritance
class Father:
    def skills(self):
        print("Father skills")
class Mother:
    def hobbies(self):
        print("Mother hobbies")
class Child(Father,Mother):
    def display(self):
        print("Child class")
c=Child()
c.display()
c.skills()
c.hobbies()
#2.
class Engine:
    def engine_type(self):
        print("Engine type")
class Wheels:
    def wheel_count(self):
        print("Wheel count")
class Car(Engine,Wheels):
    def display(self):
        print("Car class")
c=Car()
c.display()
c.engine_type()
c.wheel_count()
#multilevel inheritance
class Grandfather:
    def house(self):
        print("grand father house")
class Parent(Grandfather):
    def car(self):
        print("Parent car")
class Child(Parent):
    def bike(self):
        print("Child bike")
c=Child()
c.bike()
c.car()
c.house()
#super()
class parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def display(self):
        super().display()
        print("Age:",self.age)
c=child("Lokesh",22)
c.display()
#smalest even multiple of 2
class EvenMultiple:
    def __init__(self,n):
        self.n=n
    def find_multiple(self):
        if self.n % 2 == 0:
            return self.n
        else:
            return self.n + 1
#1.hierarchy inheritance 
class Animal:
    def eat(self):
        print("Animal Eating")
class Dog(Animal):
    def bark(self):
        print("Dog Barking")
class Cat(Animal):
    def meow(self):
        print("Cat Meowing")
d=Dog()
d.eat()
d.bark()
c=Cat()
c.eat()
c.meow()
## Parent class
class Animal:
    def shout(self):
        print("Animal is shouting")
class Dog(Animal):
    def bark(self):
        print("Bow")
class Cat(Animal):
    def meow(self):
        print("Meow")
d = Dog()
c = Cat()
d.shout()   
d.bark()    
c.shout()  
c.meow()   
#abstract class
from abc import ABC, abstractmethod         
class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rect = Rectangle(5, 3)
print("Area of the rectangle:", rect.area())   
#polymorphism     
class Shape():
    def draw(self):
        print("it is draw method")
class circle(Shape):
    def draw(self):
        print("it is circle")
c=circle()
c.draw()
#banking 