#Nov21
#Task7:
#Get one mark from student
#mark 0 to 100 otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A  ==> Even + Odd -
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL



#93 ===> A-
#99 ===> A-
#88 ====> B+

#78

#VALID MARK
#PASS MARK
#C+


a = int(input("Please enter your mark : "))
if a > 0 and a <= 100:
    print("mark is valid")
    if a >= 50:
        print("Pass Mark")
        if a >= 90 and a % 2 == 0 :
            print("A+")
        elif a >= 90 and a % 2 != 0:
            print("A-")
        elif a >= 80 and a % 2 == 0:
            print("B+")
        elif a >= 80 and a % 2 != 0:
            print("B-")
        elif a >= 70 and a % 2 == 0:
            print("C+")
        elif a >= 70 and a % 2 != 0:
            print("C-")
        elif a >= 60 and a % 2 != 0:
            print("D+")
        elif a >= 60 and a % 2 != 0:
            print("D-")
        elif a >= 50 and a % 2 == 0:
            print("E+")
        elif a >= 50 and a % 2 != 0:
            print("E-")
    else:
        print("Fail Mark")
else:
    print("Invalid Mark")
    


"""OUTPUT :

= RESTART: C:\Users\Admin\AppData\Local\Programs\Python\Python310\Nov21task7.py
Please enter your mark : 98
mark is valid
Pass Mark
A+

= RESTART: C:\Users\Admin\AppData\Local\Programs\Python\Python310\Nov21task7.py
Please enter your mark : 60
mark is valid
Pass Mark
E+

= RESTART: C:\Users\Admin\AppData\Local\Programs\Python\Python310\Nov21task7.py
Please enter your mark : 55
mark is valid
Pass Mark
E-

= RESTART: C:\Users\Admin\AppData\Local\Programs\Python\Python310\Nov21task7.py
Please enter your mark : 22
mark is valid
Fail Mark

= RESTART: C:\Users\Admin\AppData\Local\Programs\Python\Python310\Nov21task7.py
Please enter your mark : 83
mark is valid
Pass Mark
B-
"""





    
