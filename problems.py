''' #palindrome
text =input("enter the txt:").lower().replace(" ","")
if text == text[::-1]:
  print("palidrome")
else:
    print("not a palindrome")  '''


'''#character frequency counter
text = input("enter the txt:")
checked=""
for ch in text:
   if ch not in checked:
      print(ch,text.count(ch))
      checked += ch '''

'''#find the largest number in a list
numbers = [10, 2, 9, 1, 3]
lar=numbers[0]
for i in numbers:
   if i > lar:
      lar=i
print("largest number is:",lar)'''


'''#odd and even number
num = int(input("enter a num"))
if num % 2 == 0:
   print("even")
else:
   print("odd")'''

#ATM Withdrawal Validation
bal = 10000
withdraw = int (input("enter amount:\t"))
if withdraw > 0:
   if  withdraw % 100 == 0:
        if withdraw <= bal:
         print("withdrawal successful")
        else :
           print("insufficient balance")
   else:
      print("enter amoumt mutiple of 100")
else:  
   print("enter a valid amount")

#Visitor Counter System

count =0 
def vistor():
   global count
   count += 1
   print("visitor count:",count)
vistor()
vistor()
vistor()
