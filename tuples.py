#creating tuple
a=(1,2,3)
b=("apple",3,11.0)
print(a,b)

#single element tuple
c=(5,) # comma is require for every single elem tuple
print(c)

#indexing
print(a[0])
print(a[-2])

#slicing
print(a[0:2])
print(a[::-1])

#tuple packing
x=10
y="hi"
z=1.11
tup =(x,y,z)
print(tup)

#tuple unpacking
a,b,c=tup
print(a)
print(b)
print(c)

#tuple methods

#count
t=(1,2,3,1,4,1)
print(tup.count(1))

#index
print(tup.index(2))

