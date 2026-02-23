#*
#**
#***
#****
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
#.       *
#..     **
#...   ***
#.... ****
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
#.     1
#     12
#.   123
#.  1234
t = int(input("Enter the number of rows: "))
for i in range(1, t + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
#A
#AB
#ABC
#ABCD
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):           
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()
#.    A
#.   AB
#.  ABC
#. ABCD
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):   
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()