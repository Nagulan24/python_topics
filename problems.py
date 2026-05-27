#palindrome
text =input("enter the txt:").lower().replace(" ","")
if text == text[::-1]:
  print("palidrome")
else:
    print("not a palindrome")  


#character frequency counter
text = input("enter the txt:")
checked=""
for ch in text:
   if ch not in checked:
      print(ch,text.count(ch))
      checked += ch

#find the largest number in a list
numbers = [10, 2, 9, 1, 3]
lar=numbers[0]
for i in numbers:
   if i > lar:
      lar=i
print("largest number is:",lar)
