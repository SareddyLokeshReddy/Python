f = open("file1.txt", "w")
f.write("This is file handling in python")
f.close()

f=open("file1.txt","r")
print(f.read())
f.close()

f=open("file1.txt","a")
f.write("This is the python ")
f.close()

f=open("file2.txt","x")
f.close()

f=open("file2.txt","w")
f.write("This is the file handling in python ")
f.close()
