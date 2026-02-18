#Check whether a number is Prime
from rpds import List


num = int(input("Enter a number: "))

if num <= 1:
    print("It is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not prime")
            break
    else:
        print("It is prime")
#Check Palindrome Number
num =str(input("Enter the number: "))

if num== num[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")
    #Check Armstrong Number
num=int(input("Enter the numbe: "))
original = num
n=str(num)
count = len(n)
sum=0
for ch in n:
    digit=int(ch)
    total=digit**count
    sum+=total
    if sum==original:
        print("It is armstrong")
    else:
        print("It is not a armstrong")
#Print Fibonacci Series
n=int(input("Enter the numbe: "))
f=0
l=1
for i in range(n):
    print(f)
    next=f+l
    f=l
    l=next
#Reverse string
s=input("Enter the string: ")
rev=s[::-1]
print(rev)
#Second largest in array
a = input("Enter the numbers: ")
s = a.split()

n = []
for ch in s:
    n.append(int(ch))

large = n[0]
second = n[0]

for i in n:
    if i > large:
        second = large
        large = i
    elif i < large and i > second:
        second = i

print("Second largest number is:", second)
#Anagram check
a=str(input("Enter the name: "))
b=str(input("Enter the name: "))
c=len(a)
d=len(b)
if c==d:
    print("It is anagram")
else:
    print("It is not anagram")
#Remove duplicates
l=[10,20,30,40,50,10]
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)
#Factorial
n=int(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
#sum of natural umbers
n=int(input("Enter the number: "))
s=0
for i in range(1,n+1):
    s=s+i
print(s)
#check even or odd
n=int(input("Enter the number: "))
if n%2==0:
    print("It is even")
else:
    print("It is odd")
#fizzbuzz
n=int(input("Enter the number: "))
if n%6==0 and n%9==0:
    print("It is fizbuzz")
elif n%6==0:
    print("It is fizz")
elif n%9==0:
    print("It is buzz")
else:
    print("none")
#sum of unique elements
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        total = 0
       
        for key, value in d.items():
            if value == 1:
                total += key

        return total
#Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        min = prices[0]
        for i in range(len(prices)):
            n = prices[i] - min
            if n > sum:
                sum = n
            if prices[i] < min:
                min = prices[i]
        return sum
#length of last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for ch in s[::-1]:
            if ch==" " and c==0:
                continue
            elif ch!=" ":
                c+=1
            elif ch==" " and c>0:
                break
        return c
#count vowels
s=input("Enter the name: ")
t=0
for ch in s:
    if ch  in 'aeiou':
        t+=1 
print(t)
#remove the spaces
s=input("Enter the name: ")
t=" "
for ch in s:
    if ch!=" ":
        t+=ch
print(t)
#count the words
s = input("Enter the name: ")
t = {}
for ch in s:
    if ch in t:
        t[ch] += 1
    else:
        t[ch] = 1

print(t)
#First Unique Character in a String
s = input("Enter the name: ")
t = {}
for ch in s:
    if ch in t:
        t[ch] += 1
    else:
        t[ch] = 1
for i in range(len(s)):
    if t[s[i]] == 1:
        print(i)
        break
else:
    print(-1)
#majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        e = 0

        for n in nums:
            if c == 0:
                e = n
            if n == e:
                c += 1
            else:
                c -= 1

        return e
#2283. Check if Number Has Equal Digit Count and Digit Value
class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            t = num.count(str(i))
            f = int(num[i])
            if t != f:
                return False
        return True
#leap year
y=int(input("Enter the year: "))
if(y%4==0 and y%100!=0) or (y%400==0):
    print("It is leap year")
#vote eligibility
def vote_eligible(age):
    if age>=18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
    #maximum product of subarray
class Solution:
     def maxProduct(self, nums: List[int]) -> int:
        cmax = nums[0]
        cmin = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]

            if x < 0:
                cmax, cmin = cmin, cmax

            cmax = max(x, cmax * x)
            cmin = min(x, cmin * x)

            ans = max(ans, cmax)
        return ans
#count digits
n=int(input("Enter the number: "))
c=0
while n>0:
    n=n//10
    c+=1
print(c)
#number of segments in a string 
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
#power of a number
def power(base, exp):
    res = 1
    for i in range(exp):
        res = res * base
    return res
#robot return to origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h=0
        v=0
        for ch in moves:
            if ch == 'R':
                h+=1
            elif ch == 'L':
                h-=1
            elif ch == 'U':
                v+=1
            elif ch ==  'D':
                v-=1
        if h==0 and v==0:
            return True
        else:
            return False
#check perfect number
num=int(input("enter the number: "))
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
if s==num:
    print("It is perfect number")
#container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        p1=0
        p2=len(height)-1
        while p1<p2:
            a=max(a,(p2-p1)*min(height[p1],height[p2]))
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return a
#remove element
s=int(input("Enter the number: "))
a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    e=int(input("Enter the element: "))
    a.append(e)
print(a)
while s in a:
    a.remove(s)
print(a)
#check perfect square
import math
n=int(input("Enter the number: "))
s=int(math.sqrt(n))
if s*s==n:
    print("It is perfect square")
else:
    print("It is not perfect square")
#triangle pattern
n=int(input("Enter the number: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
print()
#Two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
#remove vowels
n=input("Enter the name: ")
t=""
v="aeiouAEIOU"
for ch in s:
    if ch not in v:
        t+=ch
print(t)
#check power of two
t=int(input("Enter the number: "))
if n>0 and (n & (n-1))==0:
    print("It is power of two")
else:
    print("It is not power of two")
#Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right]
            
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
#*
#**
#***
#****
t=int(input("Enter the number: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#****
#.***
#. **
#.  *
s=int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j<n-i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print() 
#reverse a number
s=int(input("Enter the number: "))
rev =0
while s>0:
    a=s%10
    rev=rev*10+a
    s=s//10
print(rev)
#1234
#123
#12
#1
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
print()
#painting partition problem
class Solution:
    def minTime(self, arr, k):
        
        low = max(arr)
        high = sum(arr)
        a = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.canPaint(arr, k, mid):
                a = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return a
    
    
    def canPaint(self, arr, k, limit):
        painters = 1
        total = 0
        
        for board in arr:
            total += board
            
            if total > limit:
                painters += 1
                total = board
                
                if painters > k:
                    return False
        
        return True
#sum multiples 
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                s += i
        return s
#type of triangle
class Solution:
    def triangleType(self, a: int, b: int, c: int) -> int:
        if a == b and b == c:
            return 1
        elif a == b or b == c or a == c:
            return 2
        else:
            return 3
#