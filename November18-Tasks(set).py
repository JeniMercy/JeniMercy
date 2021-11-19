#November-18
#SETS:
#Create two empty sets:
a = set()
b = set()
print(a)
print(b)

#update set1 with 7,8,9,1,2,3,4,5,0
c = {7,8,9,1,2,3,4,5,0}
a.update(c)
print(a)
'''OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks(set).py
{0, 1, 2, 3, 4, 5, 7, 8, 9}'''

#update set2 with 4,5,6,0
d = {4,5,6,0}
b.update(d)
print(b)
'''OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks(set).py
{0, 4, 5, 6}'''

#check whether set2 is subset of set1 or no ?
a = {7,8,9,1,2,3,4,5,0}
b = {4,5,6,0}
b.issubset(a)
'''OUTPUT:
no'''

#check whether both have common elements are no ?
I = a.intersection(b)
print(I)
'''OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks(set).py
{0, 4, 5}'''

#remove 8 from set 1 and set 2 ==> find the inferences
#a = {7,8,9,1,2,3,4,5,0}
#b = {4,5,6,0}
a.remove(8)
print(a)
#b.remove(8) 
#print(b)
'''OUTPUT:
{0, 1, 2, 3, 4, 5, 7, 9}
Traceback (most recent call last):
  File "C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks(set).py", line 44, in <module>
    b.remove(8)
KeyError: 8'''


#discard 0 from set1 and set2
a.discard(0)
print(a)
b.discard(0)
print(b)
'''OUTPUT:
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks(set).py
{1, 2, 3, 4, 5, 7, 9}
{4, 5, 6}'''

#find collection of both sets ===> set1 and set2
U = a.union(b)
print(U)










