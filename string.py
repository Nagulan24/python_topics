a="nagulan "

#indexing
#print(a[0])
#print(a[-1])

#slicing
print(a[0:5])#befor index 5
print(a[:])#entire string
print(a[2:])
print(a[:4])

#negative slicing
print(a[-5:-1])#before index -1
print(a[-5:])#entire string from index -5

#reverse slicing
print(a[::-1])

#print(a[-1:-6])# empty string because the start index is greater than end index

#methods
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

print(a.find("a"))# first occurrence of "a"
print(a.rfind("a"))# last occurrence of "a"
print(a.count("a"))# count of "a" in the string
print(a.isalpha())# check if all characters are alphabets

print(a.replace("a","o"))# replace "a" with "o"

b="nagulan,python,programming"
print(b)
print(b.split(","))# split the string by "_" and return a list

c=["one","two","three"]
print("_".join(c))# join the list elements with "," and return a string

print(a*7)# repeat the string 7 times

print(len(a))# length of the string

print(a+"leader")