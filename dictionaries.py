#create dict
a= {"name": "nagulan","age": 19}
print(a)

#accessing value
print(a["name"])

#adding new data

a["gender"]='male'
print(a)

#updating value
a["age"]=20
print(a)

#removing
del a["gender"]
print(a)


#del a
#print(a) #error because a is deleted

#keys
print(a.keys())

#values
print(a.values())

#items
print(a.items())

#get()
print(a.get("section")) # return  none if does not exist the value not error
