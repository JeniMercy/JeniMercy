#Nov-21
#Task4:
#Get one string from user
#extract middle letter of the string
#check whether middle letter is vowel or no


a = input("Please enter your string : ")
middle_letter = len(a) // 2
print("The middle letter is {}".format(a[middle_letter]))
if a[middle_letter] in "aeiou":
     print(" The middle letter {} is vowel".format(a[middle_letter]))
else:
     print("The middle letter {} is not vowel".format(a[middle_letter]))




"""OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21task4.py
Please enter your string : Niralya
The middle letter is a
The middle letter a is vowel

= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21task4.py
Please enter your string : 12456
The middle letter is 4
The middle letter 4 is not vowel

= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21task4.py
Please enter your string : aeiou
The middle letter is i
The middle letter i is vowel"""

