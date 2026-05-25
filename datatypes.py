# numeric types
a=10 # int
b=3.14 #float
c=23j+1 #complex
print(f"int is {a} and float is {b} and complex is {c}")

# boolean type
# d= true
e=True
f=False
#print(f"boolean value is {d} and {e}")
print(f"boolean value is {e} and {f}")

# dictionary type
g={"name":"nagulan","age":19,"city":"chennai"}
print(g)

#set type
h={1,2,3,4,5}
i={1,2,3,4,5,5,5}
# h and i are same because set does not allow duplicate values
print(h,i)

#none type
j=None
print(j)
def fun():
    print("this is a function")
res=fun()
print(res) # res will be None because fun() does not return anything    

#sequence types:

k=[1,2,3,4,5] #list
print(k)
k.append(6) #list is mutable
print(k)


l=(1,2,3,4,5) #tuple
print(l)
# l.append(6) #tuple is immutable, this will give an error

m="hello world" #string
print(m)
# m.append("!") #string is immutable, this will give an error
