#NOV-21
#Task3:
#collect one string from user, check whether the string is palindrome or not

a = str(input("Please enter your string : "))
reversed_string = a[::-1]
if a == reversed_string:
    print(" The string {} is a palindrome".format(a))
else:
    print("The string {} is not a palindrome".format(a))







"""OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21Task3.py
Please enter your string : MoM
 The string MoM is a palindrome

= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21Task3.py
Please enter your string : Mom
The string Mom is not a palindrome

= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21Task3.py
Please enter your string : niralya
The string niralya is not a palindrome

= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21Task3.py
Please enter your string : 1234321
 The string 1234321 is a palindrome"""
