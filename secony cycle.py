#recursive 
def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)
n=5
print(sum(n))
        