"""write a python program to print character from a string that are present at an even index number"""

str = input("enter the string:")
print(str)
l = len(str)
for i in range(0,l,2):
    print(str[i])

