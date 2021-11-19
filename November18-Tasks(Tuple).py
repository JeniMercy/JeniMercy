#November Tasks-18
#Tuple
#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
tuple1 = (1,4,5,6,7,8)
tuple2 = (5,6,7,8,9)
print(tuple1)
print(tuple2)

#Find the common elements between two tuples
#tuple1 = (1,4,5,6,7,8)
#tuple2 = (5,6,7,8,9)
set1 = set(tuple1)
set2 = set(tuple2)
set_inter = set1.intersection(set2)
print(tuple(set_inter))
'''OUTPUT
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks.py
(8, 5, 6, 7)
'''

#Concatenate both tuples and remove duplicates from tuple
#tuple1 = (1,4,5,6,7,8)
#tuple2 = (5,6,7,8,9)
tup = (tuple1 +tuple2)
print(tup)
print(tuple(set(tup)))
'''OUTPUT
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks.py
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
(1, 4, 5, 6, 7, 8, 9)'''

#Find the index value of 9 (after concatenation)
#tup = (1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
print(tup.index(9))
'''OUTPUT
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks.py
10'''

#multiply above elements 3 times
#tup = (1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
newtuple = tup*3
print(newtuple)
'''OUTPUT
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python310/November18-Tasks.py
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)'''




