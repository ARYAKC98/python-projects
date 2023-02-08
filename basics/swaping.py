#swap
# a = 10
# b = 20
#
# t = a
# a = b
# b = t


#without using third variable
a,b = int(input("enter first number:")),int(input("enter second number:"))
a,b = b,a
print('a=',a)
print('b=',b)