def count_sort(arr, place):
    n = len(arr)
    output = [0]*n
    count = [0]*10 #[1 0 0 0 0 0 0 0 0 0]
    for i in range(0,n):
        index = arr[i]//place
        count[index%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i = n-1
    while i>=0:
        ind = arr[i]//place
        output[count[ind%10]-1] = arr[i]
        count[ind%10]-=1
        i-=1
    for i in range(0,n):
        arr[i]= output[i]                    
def radix_sort(arr):
    max_ele = max(arr)
    place =1
    while max_ele//place>0:
        count_sort(arr, place)
        place*=10
a = [8,6,4,9,1,2]
b = [100, 201, 1, 810, 904, 6, 25]
radix_sort(b)
print(b)
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            current_area = width * min(height[left], height[right])
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)