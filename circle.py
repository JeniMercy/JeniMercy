'''Area of the circle and circumference:

area pi r * r   cicr  2 pi r
collect radius from user as integer
print area (int) in formatted way
print circumference in string format in formatted way'''

radius = int(input("enter the value:"))
pi = 3.14
Area = pi*radius**2
Circumference = 2*pi*radius
print("the area of the circle with radius {} and constant pi {} is {}".format(radius,pi,int(Area)))
print("the circumference of the circle with radius {} and constant pi {} is {}".format(radius,pi,str(Circumference)))


