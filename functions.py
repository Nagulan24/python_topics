# simple function

def greet():
    print("hi")
greet()

#function with parameters

def greet(name):
    print("hi",name)
greet("nagulan") # nagulan is arugment

#function with return value

def add(a,b,c,d):
    sum =a+b++c+d
    return sum
res = add(1,2,3,4) 
print(res)

#function with default parameter
def greeting(name="guest"):
    print("hi ", name)
greeting()
greeting("nagulan")

#function with variable number of arguments
def sum(num):
    tot = 0
    for i in num:
        tot += i
    return tot
res = sum([1,2,3,4,5,6,7,8,9,10])   
print(res)