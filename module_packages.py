# math module
import math

print(math.sqrt(16))
print(math.pow(2,3))
print(math.pi)

#random module
import random
print(random.randint(1,100))
print(random.choice(["one","two","three"]))
print(random.random())

#datetime module
import datetime
print(datetime.datetime.now())
print(datetime.date.today())   

#alias module
import math as m
m.sqrt(25)

#os module
import os
print(os.getcwd())
print(os.listdir())