#if_else
age = int(input("enter your age:"))
if age >= 18:
    print("adult")
elif age >= 13:
    print("childhood")    
else:
    print("child")

#using and or or in if else
grade = int(input("enter your grade:"))
if grade >= 90 and grade <= 100:
    print("O")
elif grade >= 80 and grade <90:
    print("A+")
elif grade >= 70 and grade <80:
    print("A")
elif grade >= 60 and grade <70:
    print("B+") 
elif grade >= 50 and grade <60:
    print("B")
elif grade >= 45 and grade <50:
    print("C")
elif grade <= 44 or grade >= 0:
    print("Fail")


#nested if
username = "nagulan"
password = 1234

if username == "nagulan":
    if password == 1234:
        print("login")
    else:
        print("invaid pass")
else: 
    print("invaild username")