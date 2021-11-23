#Nov21
#Task5:
#Get one string from user
#Find the middle letter
#find ascii value for the middle letter
#check whether ascii value is odd or even


a = input("Please enter your string : ")
middle_letter = len(a) // 2
print("The middle letter is {}".format(a[middle_letter]))
ascii_value = ord(a[middle_letter])
#print("The ascii value of  middle_letter is {}".format(ascii_value))
print("The middle letter of {} is {} and its ascii_value {}   " .format(a,a[middle_letter],ascii_value))




'''OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21task5.py
Please enter your string : niralya
The middle letter is a
The ascii value of  middle_letter is 97

= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/Nov21task5.py
Please enter your string : mercy
The middle letter is r
The ascii value of  middle_letter is 114
'''
