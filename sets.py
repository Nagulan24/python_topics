# creating a set
a={1,2,3}
print(a)

# unordered so that python store using hashing 
ss={7,6,5,4,3,2,1}
print(ss)

#creating a empty set
b=set() #correct
c={} #dictionary
print(type(b))
print(type(c))

#duplicate removal list to  set
d=[1,2,2,3,3,3,4,5]
d=set(d)
print(d)

#du[plicate removal in set
e={1,1,2,2,2,3,4,4,4,4,4,5}
print(e)# automatically remove duplicate

#set methods

#add
a.add(4)# only one element will  be add
print(a)

#update
a.update([7,6,5,"ten"])#multiple element will be add
print(a)

#remove
a.remove(7)# error if element is not present
print(a)

#discard
a.discard(7)# no error if element doesnot exist
print(a)

#union
s1={1,2,3}
s2={3,4,5}
s= s1|s2
print(s)

#intersection
s=s1&s2
print(s)

#difference
s=s1-s2
print(s)

#symmetric difference
s=s1^s2
print(s)

