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