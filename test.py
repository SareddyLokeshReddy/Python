#1.Two sum
nums = list(map(int, input("Enter number: ").split()))
t=int(input("Enter target: "))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==t:
            print([i,j])
#2.valid palindrome
s=input("Enter the string: ")
t=""
for i in s:
    if i.isalnum():
        t+=i.lower()
    if i==i[::-1]:
        print("It is valid palindrome")
    else:
        print("It is not valid palindrome")
#3.contains duplicate
nums=list(map(int, input("Enter number: ").split()))
if len(nums)!=len(set(nums)):
                  print("It contains duplicate")
else:
    print("It does not contains duplicate")
#4.group anagrams
w=input("Enter words: ").split()
g = {}
for s in w:
    k=''.join(sorted(word))
    if k not in g:
        g[k]=[]
    g[k].append(word)
print(list(g.values()))
#5.top k frequent elemnts
nums=list(map(int, input("Enter number: ").split()))
k=int(input("Enter the number: "))
f={}
for n in nums:
    if n in f:
        f[n]+=1
    else:
        f[n]=1
l=[]
for key,value in f.items():
    if value >= k:
        l.append(key)
print(l)
#6.sudoko
 b = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

valid=True
for i in b:
    s=set()
    for n in i:
        if n!=".":
            if n in s:
                valid = False
        s.add(n)
for j in range(9):
    s=set()
    for i in range(9):
        n=b[i][j]
        if n!=".":
            if n in s:
                valid=False
            s.add(n)
print(valid)
#.7.Parking slot
class Parkingslot:
    def __init__(self,big,medium,small):
        self.big=big
        self.medium=medium
        self.small=small
    def addcar(self,carType):
        if carType==1:
            if self.big>0:
                self.big-=1
                return True
        if carType==2:
            if self.medium>0:
                self.medium-=1
                return True
        if carType==3:
            if self.small>0:
                self.small-=1
                return True
p=Parkingslot(1,1,0)
print(p.addcar(1))
print(p.addcar(2))
print(p.addcar(3))
