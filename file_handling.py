#write mode
with open("practice.txt","w") as file:
    print(file.write("hello\n"))

#Read a entire file
with open("practice.txt","r") as file:
    print(file.read())

#append
with open("practice.txt","a") as file:
    print(file.write("added lines"))

#read a file line by line
with open("practice.txt","r") as file:
    print(file.readline()) # read first line
    print(file.readline()) # read second line
    

#write multi lines mode
with open("practice.txt","w") as file:
    lines =["one\n","two\n","three\n","four\n","five\n"]
    print(file.writelines(lines))

#read all lines in list
with open("practice.txt","r")as file:
    print(file.readlines())
    print(file.tell()) 

#file pointer
with open("practice.txt","r") as file:
    print(file.tell())# starting point
    print(file.read(5))#read 5 element
    print(file.tell())#tell point after read
    print(file.seek(0))#move to 0 or starting point
    print(file.tell())# tell point after moved pointer