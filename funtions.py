#functions
from operator import mul
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
n = [-2,5,-1,8,0]
result = list(filter(lambda x: x>0, n))
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
s = "abbaca"
result = remove_adjacent_duplicates(s)
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