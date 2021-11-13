"""Nov-11
Task3:
    
Get one string from user
    
    a = "computer"
    
    convert middle character to upper case
    
    a = "computer" ==> compUter
    groovyy ==> groOvyy"""

a = input("enter the string : ")
mid = int(len(a)/2)
print(a[:mid]+a[mid].upper()+a[mid+1:])







