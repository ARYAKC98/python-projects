#wrire a python program to access a function inside a function
# def outerfunc(a,b):
#     def innerfunc():
#         c = a+b
#         return c
#     return innerfunc()
# print(outerfunc(5,6))


#write a python program to create and print a list where the values are square of numbers between 1 and 30(both included)
# def values():
#     lst = list()
#     for i in range(1,31):
#         lst.append(i**2)
#     print(lst)
# values()

#assign a different name to a function and call it through the new name
# def func():
#     print("gayathri")
# new_func = func()
# (new_func)


#generate a python list of all the even numbers between 4 to 30
# def even():
#     lst = []
#     for i in range(4,30):
#         if i%2 == 0:
#             print(i)
#         lst.append(i)
# even()


#python function that accepts two numbers as arguments and returns the sum

# def sum(a,b):
#     result=(a+b)
#     print(result)
# sum(5,7)



#python functions that accepts different values as parameters and returns a list

# def values(*val):
#     lst = []
#     for i in val:
#         lst.append(i)
#     print(lst)
# values(1,"maya" ,2,"gaya")

#python function that returns tuple
# def func():
#     return "haii",233,"hello"
# print(func())


#define a function that accepts 2 values and return its sum,subtraction and multiplication
# n1 = int(input("enter the first number:"))
# n2 = int(input("enter the second number:"))
# def operator(a,b):
#     return a+b,a-b,a*b
# sum,sub,mul = operators(n1,n2)
# print("result of sum is:",sum)
# print("result of sub is:",sub)
# print("result of mul is:",mul)



#define a function that accepts a number and returns whether the student is present or absent
# rollno = int(input("enter the rollno:"))
# def student(rollno):
#     i =[1,2,3,5,6,7,8]
#     if rollno in i:
#         print("the student is present")
#     else:
#         print("the student is absent")
# student(rollno)


#define a function which counts vowels and consonents in a word
# word=input("enter the word:")
# def count(word):
#     w = 0
#     c = 0
#     v = ["a","e","i","o","u","A","E","I","O","U"]
#     for i in word:
#         for i in v:
#             w = w+1
#         else:
#             c = c+1
#     print("vowel is",w)
#     print("consonent is",c)
# count(word)


#define a function that accepts a number and returns whether the number is even or odd
# num = int(input("enter the number"))
# def even_odd(num):
#     if num % 2==0:
#         print("num is even:")
#     else:
#         print("the number is odd")
# even_odd(num)


#define a function in python that accepts three values and returns the maximum of three numbers
# def values(a,b,c):
#     if a>b and a>c:
#         print("the max no is",a)
#     elif b>a and b>c:
#         print("the max no is",b)
#     else:
#         print("the max no is",c)
# values(4,18,6)