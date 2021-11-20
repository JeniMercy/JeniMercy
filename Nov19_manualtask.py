
#Nov19_Task

#Output Prediction 

Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]


print(Li1[5][0])#11
print(Li1[5][6])#6666
print(Li1[5][-2])#6666
print(Li1[5][7])#7777
print(Li1[6])#7777
print(Li1[5][5][1])#222
print(Li1[-2][-1])#7777


print(Li1[2][2:4])#error
