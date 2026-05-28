'''#zero division error
try:
    num= int(input("enter a number:"))
    res = 10/num
    print(res)
except ZeroDivisionError:
    print("cannot divide by zero")'''

'''#value error
try:
    num2 = int(input("enter a number:"))
except ValueError:
    print("invalid input")'''

'''#multiple exceptions
try:
    num3= int(input("enter number:"))
    res=10/num3
    print(res)
except ZeroDivisionError:
    print("zero cant be divided")
except ValueError :
    print("invalid input")'''

'''#catich all exceptions without specific error type
try:
    num4=int(input("enter number:"))
    res = 10/num4
    print(res)
except Exception as e:
    print("error:",e)'''

'''else block
try:
    num5=int(input("enter number:"))
    res = 10/num5
    print(res)
except Exception as a:
    print("error:",a)
else :
    print("program executed successfully") #excute only when no exception occur'''

'''#finally
try:
    num6= int(input("enter number:"))
except Exception as b :
    print("error:",b)
finally :
    print("end of program") #execute always '''

#raise exception
def check_age():
    age = int(input("enter age:"))
    if age <0:
        raise ValueError("age cant be newgative")
    else:
        print("age is valid")
check_age()