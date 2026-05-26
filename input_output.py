a=input()
print(type(a))

#taking input and converting it to integer
a=int(input())

#taking multiple inputs

c,b=input().split()
print(c)
print(b)

#taking multiple inputs and converting them to integer
x,y=map(int,input().split())
print(type(x))
print(type(y))

#output
print("Hello, World!")

#formatted string
name=input("Enter your name: ")
age=int(input(("Enter your age: ")))
print(f"My name is {name} and I am {age} years old.")

#escape characters
print("a \n b \t c \\ d \" e")
