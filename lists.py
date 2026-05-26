#creating list
num=[10,20,"nagulan",30.5,True]
print(num)

#indexing
print(num[0])
print(num[-1])

#slicing
print(num[0:3])
print(num[::2])
print(num[:3])

#methods

#append
num.append("python")
print(num)

#insert
num.insert(2,"programming")
print(num)

#extend
num.extend(["java"])
print(num)

#remove
num.remove("nagulan")
print(num)

#pop
num.pop(2)
print(num)

#index
print(num.index("python"))

#sort
numbers=[5,2,9,1,3]
numbers.sort()
print(numbers)

#reverse
a=[1,2,3,4,5]
a.reverse()
print(a)