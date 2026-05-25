#arithmetic operators
a=3
b=3
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division, result is float  
print(a//b) # floor division(how many times division can done)eg 120//20=6, 100//20=5)
print(a%b) # modulus, remainder
print(a**b) # exponentiation


#comparison operators
x=10
y=20
print(x==y) # equal to
print(x!=y) # not equal to
print(x>y) # greater than 
print(x<y) # less than

#Assignement operators
p=10
print(p) # 10
p+=1
print(p) # 20


#logical operator
c=10
d=20
print(c and d) # logical and
print(c or d) # logical or
print(not c) # logical not, it will return False because c is non-zero value

#membership operator
list1=[1,2,3,4,5]
print(5 in list1) # True
print(5 not in list1) # False

#identity operator
e=10
f=10
print(e is f) # True, because small integers are cached by Python and point to the same memory location
print(e is not f) # False

print(id(e)) 
print(id(f)) 

#bitwise operators
g=5 # in binary 0101
h=3 # in binary 0011
print(g & h) # bitwise AND, result is 1 (in binary 0001)
print(g | h) # bitwise OR, result is 7 (in binary 0111)
print(g ^ h) # bitwise XOR, result is 6 (in binary 0110)
print(~g) # bitwise NOT, result is -6 (in binary 1010
print(g << 1) # left shift, result is 10 (in binary 1010)
print(g >> 1) # right shift, result is 2 (in binary 001