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