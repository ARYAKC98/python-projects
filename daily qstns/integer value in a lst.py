"""write a program to print integer value in a list using list comprehension"""

lst = [12,66,14,5,12,8,12,2,4,11,22]
result = [x for x in lst if type(x)==int]
print(result)
