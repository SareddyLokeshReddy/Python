#functions
from operator import mul
from os import remove
from os import remove
from typing import List

from matplotlib.pylab import number


def say_hello():
    print("Hello, welcome to Python!")
say_hello()
#add
def add(a, c):
    return a + c

print(add(5, 3))
#mul
def add(a, b):
    return a * b

print(mul(3, 3))
#name
def welcome(name):
    print("Welcome,", name)

welcome("Python learner")
#square
def square(s):
    return s * s



print(square(4))
#even or odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)
#Given an array of integers nums, return the number of good pairs.A pair (i, j) is called good if nums[i] == nums[j] and i < j.
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count={}
        pairs=0
        for num in nums:
            if num in count:
                pairs+=count[num]
                count[num]+=1
            else:
                count[num]=1
        return pairs
#A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).Return the number of indices where heights[i] != expected[i].
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        b=[]
        for i in nums:
            a.append(i*i)
        a.sort()
        return a

#circle area
def circle_area(r):
    pi=3.114
    a=pi*r*r
    return a
#area of rectangle
def rectangle_area(l,b):
    return l*b
print(rectangle_area(4,5))
#factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    print(factorial(5))
    #fibonacci
    def fibonacci(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)
        print(fibonacci(6))
    #prime number
    def is_prime(num):
        if num <= 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
    return True

#reverse string
def reverse_string(s):
    return s[::-1]
a="Hello World"
print(reverse_string(a))
#palindrome
def is_palindrome(s:str):
    s="madam"
    if s==s[::-1]:
        return True
    else:
        return False
    #anagram
    def is_anagram(s1,s2):
        s1="listen"
        s2="silent"
        if sorted(s1)==sorted(s2):
            return True
        else:
            return False
#largest number in list
def largest_number(n):
    n=[3,5,6,7,2,9]
    return max(n)
#smallest number in list
def is_smallest_number(n):
    n=[3,4,5,6,1,8]
    return min(n)
#count vowels in string
def count_vowels(s):
    s="hello world"
    count=0
    for i in s:
        if i.lower() in 'aeiou':
            count+=1
    return count
#remove duplicates from list
def remove_duplicates(n):
    n=[1,2,3,4,5,6,7,8,1,2,3]
    return list(set(n))
#merge two lists
def merge_lists(l1,l2):
    l1=[1,2,3]
    l2=[4,5,6]
    return l1+l2
#find second largest number in list
def second_largest(n):
    n=[1,2,3,4,5]
    n=list(set(n))
    n.sort()
    return n[-2]
#find second smallest number in list
def second_smallest(n):
    n=[5,4,3,2,1,8]
    n=list(set(n))
    n.sort()
    return n[1]
#count words in string
def count_words(s):
    s="Lokesh"
    w=s.split()
    return len(w)
#find factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    print(factorial(5))
    #conditional statements
    x=25
    if x>20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")
    #contains duplicate 2
    def containsDuplicate(nums: List(int))->bool:
        numsset=set()
        for num in nums:
            if num in numsset:
                return True
            numsset.add(num)
            return False
#maxmimum product
class Solution:
    def maxProduct(self, nums:List[int])->int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
#factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#Sum of digits
def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10+sum_of_digits(n/10)
    print(sum_of_digits(1234))
    #power of a number
    def power(base,exp):
        if exp ==0:
            return 1
        else:
            return base*power(base,exp-1)
        print(power(2,3))

#product of three numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        p1 = nums[-1] * nums[-2] * nums[-3]
        p2 = nums[0] * nums[1] * nums[-1]
        return max(p1,p2)
                
 #dictionary
lst={'ram':20,'krish':23,'shyam':21,'radha':25,'chandu':22}
for k,v in lst.items():
    if v==25:
        print(k,v)
#list
r=[10,20,16,23,12,25,16,16,10,20]
dic={}
for i in r:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
#reverse words in a string
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s)
#reverse string prefix
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        d1 = s[:k][::-1]
        d2 = s[k:len(s)]
        return d1 + d2
#even or odd
def check_even_odd(n):
    for num in n:
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
nums = [10, 23, 45, 68, 90, 13]
check_even_odd(nums)
#can we make arthimetic progression from given array
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[0] - arr[1]
        for i in range(2,len(arr)):
            if arr[i-1] - arr[i] != d:
                return False
        return True
#return true if string contains vowels
def contains_vowels(n):
    for char in n:
        if char.lower() in 'aeiou':
            return True
    return False
s = "Hello"
print(contains_vowels(s))
#Maximum Product of Two Elements in an Array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
     max=0
     n=len(nums)
     for i in range(n):
        for j in range(n):
            if i!=j:
                v=(nums[i]-1 )* (nums[j]-1)
                if v>max:
                    max=v
     return max
#count elements with maximum frequency
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {} 
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        max_n = max(d.values())

        count = 0
        for value in d.values():
            if value == max_n:
                count += value
        return count
#count elements with minimum frequency
class Solution:
    def minFrequencyElements(self, nums: List[int]) -> int:
        d = {} 
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        min_n = min(d.values())

        count = 0
        for value in d.values():
            if value == min_n:
                count += value
        return count
#find missing elements
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        TypeError = len(nums)
        for i in range(t):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
#truncate sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        return " ".join(s[:k])
#first 10 natural numbers sum
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first", n, "natural numbers is:", sum)
#chech whether the number is palindrome or not
def is_plindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    else:
        return False
#third maximum number in list
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
#number of senior citizens
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1
        return count
#reverse words in a strin III
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = []
        for w in words:
            res.append(w[::-1])
        return " ".join(res)
#lambda function add
add = lambda a, b: a + b
print(add(5, 3))
#lambda function multiplication
mul = lambda a, b: a * b
print(mul(5, 3))
#lambda function division
div = lambda a, b: a / b
print(div(10, 2))
#lambda function square
square = lambda x: x * x
print(square(4))
#filter
#1 return the divided by 2 numbers
n = [1,2,3,4,5,6]
result = list(filter(lambda x: x%2==0, n))
print(result)
#2 return the greater than 10
n = [5,12,7,18,3]
result = list(filter(lambda x: x>10, n))
print(result)
#3
t = [-2,5,-1,8,0]
result = list(filter(lambda x: x>0, t))
print(result)
#4

n = [10,12,15,7,20]
result = list(filter(lambda x: x%5==0, n))
print(result)
#5
w = ["ram","varun","ravi","lokesh"]
result = list(filter(lambda x: len(x)>4, w))
print(result)
#removing stars from a string
s = "he*ll*o w*or*ld"
result = s.replace("*", "")     
print(result)
#removing all adjacent duplicates from a string
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
t = "abbaca"
result = remove_adjacent_duplicates(t)
print(result)
#map function
#1 return the square of numbers
n = [1,2,3,4,5]
result = list(map(lambda x: x*x, n))
print(result)
#2 return the length of words
w = ["hello", "world", "python"]
result = list(map(lambda x: len(x), w))
print(result)
#3 return the uppercase of words
w = ["hello", "world", "python"]
result = list(map(lambda x: x.upper(), w))
print(result)
#transpose of a matrix
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
print(result)
def operation(func):
 def wrapper(a, b):
        print("Addition:", a + b)
        print("Multiplication:", a * b)
        return func(a, b)
        return wrapper
@operation
def user(a, b):
    print("User inputs:", a, b)
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
user(a, b)
#sorted squares of a list
def sorted_squares(nums):
    return sorted(x*x for x in nums)
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)
#find the number of good pairs
def num_identical_pairs(nums):
    count = {}
    pairs = 0
    for num in nums:
        if num in count:
            pairs += count[num]
            count[num] += 1
        else:
            count[num] = 1
    return pairs
nums = [1, 2, 3, 1, 1, 3]
result = num_identical_pairs(nums)
print(result)
#backspace string compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(s):
            stack = []
            for ch in s:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack
        return remove(s) == remove(t)
#find the difference of two arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
#Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        s1 = s[:half]
        s2 = s[half:]

        vowels = "aeiouAEIOU"
        count1 = 0
        count2 = 0
        for i,j in zip(s1,s2):
            if i in vowels:
                count1 += 1
            if j in vowels:
                count2 += 1
        return count1 == count2
#sum of subarray minimums
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = 0
        mod = 10**9 + 7

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += arr[j] * (i - j) * (j - k)
            stack.append(i)

        return result % mod
#reverse String II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), 2 * k):
            res.append(s[i:i + k][::-1])
            res.append(s[i + k:i + 2 * k])
        return ''.join(res)
#consequtive ones 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
#amstrong number in a list
def amstrong_numbers(nums):
    result = []
    for num in nums:
        s = str(num)
        n = len(s)
        armstrong_sum = sum(int(digit) ** n for digit in s)
        if armstrong_sum == num:
            result.append(num)
    return result
#palindrome number in list
def palindrome_numbers(nums):
    return [num for num in nums if str(num) == str(num)[::-1]]
nums = [121, 123, 454, 789, 11]
result = palindrome_numbers(nums)
print(result)
#maximum product of two elements in an array
class Solution:
    def maxProduct(self, n: int) -> int:
        t=1
        r=list(map(int, str(n)))
        r.sort()
        return r[-1]*r[-2]
#find the number of good pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count={}
        pairs=0
        for num in nums:
            if num in count:
                pairs+=count[num]
                count[num]+=1
            else:
                count[num]=1
        return pairs
#third maximum number in list
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
#maximum product of two elements in an array
class Solution:
    def maxProduct(self, n: int) -> int:
        t=1
        r=list(map(int, str(n)))
        r.sort()
        return r[-1]*r[-2]  
#find the difference of two arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
#find the number of good pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count={}
        pairs=0
        for num in nums:
            if num in count:
                pairs+=count[num]
                count[num]+=1
            else:
                count[num]=1
        return pairs
#1.⁠ ⁠Python Functions
# add numbers
def add(a,b):
    return(a+b)
print(5+6)

#Create a function to check whether a number is even or odd.
def even_or_odd(num):
    if num % 2==0:
        return "even"
    else:
        return "false"
print(even_or_odd(10))
#Write a function to find the factorial of a number.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#Create a function that returns the largest among three numbers.
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and  b>a:
        return b
    else:
        return c
print(largest(10,20,30))
#Write a function to count vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count
print(count_vowels("lokesh"))
#Create a function to reverse a string.
def reverse(text):
    s=text[::-1]
    return s
print(reverse("lokesh"))
#Write a function to calculate the sum of elements in a list.
def sum(a):
    if len(a)==0:
        return 0
    else:
        return a[0]+sum(a[1:])
list=[1,2,3,4,5]
print(sum(list))
#Create a function to check whether a string is a palindrome.
def palindrome(t1):#
    if t1==t1[::-1]:
        return "it is a plaindrome"
    else:
        return "It is not a plaindrome"
print(palindrome("121"))
#Write a function to find the minimum element in a list.
def find_min(num):
    min = num[0]

    for num in num:
        if num < min:
            min = num

    return min
print(find_min([2,3,1,4,5]))
#Create a function that converts Celsius temperature into Fahrenheit.
def cel_to_fah(c):
    f=(c*9/5)+32
    return f
print(cel_to_fah(30))

#arguments
#Write a function using positional arguments to multiply two numbers.
def add(a,b):
    print(a+b)
add(5,6)
#Create a function using keyword arguments to display student details.
def student(name,branch):
    print(name +" "+  branch)
student(name="lokesh",branch="cse")
#Write a function with a default argument for country name.
def name(n="India"):
    print("Hello"+n)
name()
#Create a function that takes three arguments and prints their average.
def ave(a,b,c):
    t = (a+b+c)/3
    return t
print(ave(10,20,30))
#Write a function with default values for username and password.
def details(Username="lokesh",password="1234"):
    print(Username+" "+password)
details()
#Create a function that accepts marks of five subjects as arguments.
def marks(a,b,c,d,e):
    print(a,b,c,d,e)
marks(10,20,30,40,50)
#Write a function to calculate simple interest using arguments.
def si(p,t,r):
    s=(p*t*r)/100
    print(s)
si(10,20,30)
#Create a function using mixed positional and keyword arguments.
def mix(n,name):
    print(n+name)
mix("9",name="lokesh")
#Write a function that accepts name and age, then prints eligibility for voting.
def vote(name,age):
    if age <=18:
        print(name+"He is eligible")
    else:
        print(name+"not eligible")
vote("lokesh",18)
#Create a function using default arguments to calculate area of rectangle.
def area(l=5,b=20):
    print(l*b)
area()
#3.⁠ ⁠Python *args / **kwargs
#Write a function using *args to find the sum of numbers.
def sum_numbers(*args):
    t=0
    for n in args:
        t+=n
    return t
print(sum_numbers(1,2,3))
#Create a function using *args to find the largest number.
def largest(*args):
    lar=args[0]
    for n in args:
        if n>lar:
            lar=n
        else:
            lar=args[0]
    return lar
print(largest(1,2,3,4,5))
#Write a function using **kwargs to print student details.
def student(**kwargs):
    print(kwargs["name"]+" "+kwargs["branch"])
student(name="lokesh",branch="cse")
#Create a function using **kwargs to display employee information.
def employee(**kwargs):
    print(kwargs["id"]+" "+kwargs["name"]+" "+kwargs["department"])
employee(id="1",name="lokesh",department="HR")
#Write a function using *args to calculate average.
def ave(*args):
    if len(args)==0:
        return 0
    t=sum(args)
    ave=t/len(args)
    return ave
print(ave(1,2,3,4))
#Create a function using *args to multiply all numbers.
def mul(*args):
    t=1
    for n in args:
        t*=n
    return t
print(mul(1,2,3,4))
#Write a function using **kwargs to print key-value pairs.
def pairs(**kwargs):
    print(kwargs)
pairs(id=1,value="lokesh")
#Create a function using both *args and **kwargs.
def both(*args, **kwargs):
    print(args)
    print(kwargs)
both(1, 2, 3, name="Lokesh", age=21)
#Write a function that counts total arguments passed using *args.
def count(*args):
    c=len(args)
    print(c)
count(1,2,3,4)
#Create a function to display product details using **kwargs.
def details(**kwargs):
    print(kwargs)
details(id=1,name="rice",location="hyd")

# Python Class Methods Programs
# 1.⁠ ⁠Create a method to display student information.
class Student:
    def __init__(self, name, depart):
        self.name=name
        self.depart=depart
    def display(self):
        print("Name:",self.name)
        print("Depart:",self.depart)
s1=Student("Lokesh","CSE")
s1.display()

# 2.⁠ ⁠Create a method to calculate addition.
class Addition:
    def add(self, a, b):
        return a + b
a1 = Addition()
print(a1.add(5, 4))
# 3.⁠ ⁠Create a method returning square of a number.
class Square:
    def square(self,a):
        return a*a
s=Square()
print(s.square(4))


# 4.⁠ ⁠Create a method to update employee salary.
class emp:
    def __init__(self,name):
        self.name=name
    def set_name(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
e1=emp("Lokesh")
print("Before:")
e1.display()
e1.set_name("Ravi")
print("After")
e1.display()#

# 5.⁠ ⁠Create a class method using ⁠ @classmethod ⁠.
class Emp:
    def __init__(self, name):
        self.name = name

    @classmethod
    def add(cls, emp_id):
        cls.id = emp_id

    def display(self):
        print("Name:", self.name)
        print("ID:", Emp.id)

Emp.add(101)
e1 = Emp("Lokesh")
e1.display()
# 6.⁠ ⁠Create a static method using ⁠ @staticmethod ⁠.
class detail:
    @staticmethod
    def name(sname):
        return sname
r=detail.name("Lokesh")
print("Name:",r)
# 7.⁠ ⁠Create multiple methods in one class.
class stu:
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
    def sub(a,b):
        return a-b
r=stu.add(5,4)
r1=stu.mul(5,4)
r2=stu.sub(5,4)
print("add:",r)
print("mul:",r1)
print("sub:",r2)
r2=stu.sub(5,4)
print("add:",r)
print("mul:",r1)
print("sub:",r2)

#8.⁠ ⁠Create a method calling another method.
class A:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
a=A("Lokesh")
a.display()
# 9.⁠ ⁠Create a method to check even or odd.
class evenorodd:
    def __init__(self,a):
        self.a=a
    def div(self):
        if self.a%2==0:
            print("It is even")
        else:
            print("It is odd")
e=evenorodd(10)
e.div()
## Python Inheritance Programs
#1.⁠ ⁠Create single inheritance using ⁠ Animal ⁠ and ⁠ Dog ⁠.
class Animal:
    def sound(self):
        print("bark")
class dog(Animal):
    def bark(self):
        print("Dog barks")
d1=dog()
d1.sound()
d1.bark()
# 2.⁠ ⁠Create multilevel inheritance example.
class Lion:
    def first(self):
        print("It is Big")
class Bare(Lion):
    def second(self):
        print("it is small")
class deer(Bare):
    def third(self):
        print("It is a very small")
d=deer()
d.first()
d.second()
d.third()
# 3.⁠ ⁠Create hierarchical inheritance example.
class Human:
    def work(self):
        print("human can work")
class Eat(Human):
    def eat(self):
        print("It is eating")
class Run(Human):
    def run(self):
        print("It is running")
e=Eat()
e.work()
e.eat()
t=Run()
t.work()
t.run()
#4.⁠ ⁠Create multiple inheritance example.
class Animal:
    def sound(self):
        print("Sounds")
class dog(Animal):
    def bark(self):
        print("It is barking")
class cat(dog):
    def meow(self):
        print("it is meow")
r=cat()
r.meow()
r.bark()
# 5.⁠ ⁠Demonstrate method overriding.
class Animal:
    def sound(self):
        print("it is sound")
class dog:
    def sound(self):
        print("It is bow")
d=dog()
d.sound()
# 6.⁠ ⁠Use ⁠ super() ⁠ in inheritance.
class Parent:
    def __init__(self):
        print("Parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()   
        print("Child constructor")
c = Child()

#Subtract the Product and Sum of Digits of an Integer – Simple Digit Traversal Approach
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        t=str(n)
        for i in t:
            d=int(i)
            s+=d
            p*=d
        return p-s
#max subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            m=max(m,c)
        return m
#find difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r={}
        for ch in t:
            if ch in r:
                r[ch]+=1
            else:
                r[ch]=1
        for c in s:
            if c in r:
                r[c]-=1
            else:
                r[c]=1
        for key,value in r.items():
            if value==1:
                return key
#2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in range(len(s)):
            if dic[s[i]]==1:
                return i
        return -1
#3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                r.append(nums1[i])
        return list(set(r))
#4
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                r.append(nums1[i])
                nums2.remove(nums1[i])
        return list((r))
#5
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                r.append(nums1[i])
        return list(set(r))
#class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l
class Solution:
    def isHappy(self, n: int) -> bool:
        r = set()
        while n != 1 and n not in r:
            r.add(n)
            s = 0
            for i in str(n):
                s += int(i) ** 2
            n = s
        return n == 1
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        r=0
        for i in stones:
            if i in jewels:
                r+=1
        return r
class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=0
        while num>0:
            if num%2==0:
                num//=2
                n+=1
            else:
                num-=1
                n+=1
        return n
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            if n==2**i:
             return True
        else:
            return False
#addition
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

res = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    res.append(row)

print(res)
#substraction
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

res = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    res.append(row)

print(res)
class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            t = 0
            for j in str(nums[i]):
                t += int(j)
            nums[i] = t
        return min(nums)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left = 0
            right = len(row) - 1
            while left <= right:
                row[left],row[right] = 1 - row[right], 1- row[left]
                left += 1
                right -= 1
        return image
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        t = sum(cost)
        for i in range(2,len(cost),3):
            t -= cost[i]
        return t
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r={}
        for i in range(len(mat)):
            c=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    c+=1
            r[i]=c
        s=sorted(r,key=r.get)
        return s[:k]
        class Solution:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=[]
        for i in range(len(accounts)):
            sum=0
            for j in range(len(accounts[0])):
                sum+=accounts[i][j]
            s.append(sum)
        return max(s)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    c+=1
        return c
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    c+=1
        return c
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r=[]
        for i in range(len(matrix)):
            m=min(matrix[i])
            c=0
            for j in range(len(matrix[0])):
                if matrix[j][matrix[i].index(m)]>m:
                    c+=1
            if c==len(matrix)-1:
                r.append(m)
        return r
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        
        while l <= r:
            m = (l + r) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                r = m - 1
            else:
                l = m + 1
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        t=0
        for s in sentences:
            t=max(t,len(s.split()))
        return t
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            f=matrix[mid]
            l=0
            r=len(f)-1
            while l<=r:
                m=(l+r)//2
                if f[m]==target:
                    return True
                elif f[m]>target:
                    r=m-1
                else:
                    l=m+1
            if f[-1]>target:
                right=mid-1
            elif f[-1]<target:
                left=mid+1
        return False
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(target)<ord(i):
                return i
        return letters[0]
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1
        ans=letters[0]
        while l<=r:
            m=(l+r)//2
            if ord(letters[m])>ord(target):
                ans=letters[m]
                r=m-1
            else:
                l=m+1
        return ans
#big sum
def aVeryBigSum(ar):
    r=0
    for i in ar:
        r+=i
    return r
#plus minus    
def plusMinus(arr):
    n=len(arr)
    p=0
    N=0
    z=0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            N+=1
        else:
            z+=1
    print(p/n)
    print(N/n)
    print(z/n)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num = len(nums)
        for i in range(num):
            for j in range(num - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
         return (max(nums) - min(nums)) * k
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=0
        for i in range(1,len(nums)):
            if nums[i]>nums[n]:
                n=i
        return n
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        v=False
        for i in matrix:
            for j in range(len(i)):
                if i[j]==target:
                    v=True
        return v
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1

        return l
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in range(len(hours)):
            if hours[i]>=target:
                c+=1
        return c
class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        pairs=[]
        for key in freq:
            pairs.append([freq[key],key])
            pairs.sort(reverse=True)
        ans=""
        for char,count in pairs:
            ans+=count*char
        return ans
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d=0
        for i in str(n):
            d+=int(i)
        return d
def diagonalDifference(arr):
    n = len(arr)
    f = 0
    l = 0
    for i in range(n):
        f += arr[i][i]
        l += arr[i][n - i - 1]
    return abs(f-l)
def birthdayCakeCandles(candles):
    m=candles[0]
    c=0
    for i in candles:
        if i >m:
            m=i
            c=1
        elif i==m:
            c+=1
    return c
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s)-1):
            if abs(int(s[i])-int(s[i+1])) > 2:
                return False
        return True
class Solution:
    def passwordStrength(self, password: str) -> int:
        s=set(password)
        c=0
        for i in s:
            if i.islower():
                c+=1
            elif i.isupper():
                c+=2
            elif i.isdigit():
                c+=3
            else:
                c+=5
        return c
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2)-min(nums1)
def insertionSort1(n, arr):
    key=arr[n-1]
    i=n-2
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        print(*arr)
        i-=1
    arr[i+1]=key
    print(*arr)
class Solution:
    def processStr(self, s: str) -> str:
        r=[]
        for i in s:
            if i.isalpha():
                r.append(i)
            elif i=="*":
                if r:
                    r.pop()
            elif i=="#":
                r.extend(r)
            elif i=="%":
                r=r[::-1]
        return "".join(r)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        r=[]
        for key,value in d.items():
            if key==value:
                r.append(key)
        if len(r)!=0:
            return max(r)
        return -1
 
