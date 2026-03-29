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
        