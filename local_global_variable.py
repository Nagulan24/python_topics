#local variable 
def greet():
    x=1
    print(x)
greet()

# global variable

x= 10 # can access anywhere in program
def val():
    print(x)
val()
    

# variable priority local > global

y=10 # 2nd priority
def dis():
    y =20 # 1st priority
    print(y)
dis()
print(y)

#global keyword
Z= 10
def display():
    global Z
    Z = Z+5
    print(Z) 
display()
print(Z)# modified global variable

'''#without global keyword

A= 10
def show():
    A= A+5 # cant be modify global variable
    print(A)
show() # UnboundLocalError'''
