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
