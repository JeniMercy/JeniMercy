'''Get radius (int) and height (float) from user using input function
Find the area of cylinder pi r*r h 
Print area output in integer with formatted output
'''
radius = int(input("enter the value:"))
height = float(input("enter the value:"))
pi = 3.14
Area = pi*radius*radius*height
print("the area of cylinder with radius {} and height {} and constant pi {} is {}".format(radius,height,pi,int(Area)))

             
