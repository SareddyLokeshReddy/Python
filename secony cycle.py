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
from os import name

from rpds import List         
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
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class CreditCardPayment(Payment):
    def pay(self):
        print("Credit Card Payment")
class UPIPayment(Payment):
    def pay(self):
        print("UPI Payment")
class NetBankingPayment(Payment):
    def pay(self):
        print("Net Banking Payment")
c = CreditCardPayment()
u = UPIPayment()
n = NetBankingPayment()
c.pay()
u.pay()
n.pay()
#abstract method
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area")
    def perimeter(self):
        print("Circle Perimeter")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area")
    def perimeter(self):
        print("Rectangle Perimeter")

c = Circle()
r = Rectangle()
c.area()
c.perimeter()
r.area()
r.perimeter()
#temparature control
class Temp:
    def __init__(self):
        self.__celsius = 0
    def set_temp(self, c):
        self.__celsius = c
    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
t = Temp()
t.set_temp(25)
print("Fahrenheit:", t.to_fahrenheit())
#method overidding
class Parent:
    def show(self):
        print("Parent class method")
class Child(Parent):
    def show(self):
        print("Child class method")
p = Parent()    
# Check if All A's Appears Before All B's
class Solution:
    def checkString(self, s: str) -> bool:
        a = "".join(sorted(s))
        return a == s
# Check if the Sentence Is Pangram
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set('abcdefghijklmnopqrstuvwxyz').issubset(set(sentence))        
#Array Partition
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0,len(nums),2):
            sum += nums[i]
        return sum
#Harshad number
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=str(x)
        t=0
        for i in  s:
            t+=int(i)  
        if x%t==0:
            return t
        else:
            return -1
#candy distribution
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a = set(candyType)
        t = int(len(candyType) / 2)
        if len(a) == t or len(a) > t:
            return t
        elif len(a) < t:
            return len(a)
#employee details      
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
#N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0 or n==1:
            return n
        if n==2:
            return 1
        T = [0] * (n+1)
        T[0] = 0
        T[1] = T[2] = 1
        for i in range(3,n+1):
            T[i] = T[i-1] + T[i-2] + T[i-3]
        return T[n]
"""1. Class & Object
Create a class Student Attributes:
name
age
marks
Method:
display()
Create 3 objects and print details."""
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("marks:",self.marks)
s1=Student("lokesh",22,25)
s2=Student("ravi",20,21)
s3=Student("ram",19,23)
s1.display()
s2.display()
s3.display()
""". Constructor
Create class Employee
Constructor should accept:
name
department
salary
Create method:
show_details()
Create 2 objects."""
class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def show_details(self):
        print("name:",self.name)
        print("department:",self.department)
        print("salary:",self.salary)
e1=Employee("Lokesh","HR",5000)
e2=Employee("Ravi","Manager",100000)
e1.show_details()
e2.show_details()