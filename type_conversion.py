#type conversion

#1. implicit type conversion
a=10 # int
b=3.14 #float
c= a+b # int is converted to float
print(c)

#2. explicit type conversion
d=10 
print(type(d),d) # int
e=float(d) 
print(type(e),e) # float

f=3.14
print(type(f),f) # float    
g=int(f)
print(type(g),g) # int, decimal part is truncated or removed

h="a"
print(type(h),h) # string
i=bool(h)
print(type(i),i) # boolean, non-empty string is True

j=""# empty string only False
print(type(j),j) # string
k=bool(j)
print(type(k),k) # boolean, empty string is False