#reverse a string
# str1 = str(input("enter the string:"))
# def reverse(str1):
#     print(str1[::-1])
# reverse(str1)


#calculator function
# def calculator(a,b):
#     def addition():
#         c = a+b
#         return c
#     return addition()+5
# print(calculator(4,4))


#even numbers betweeen 4 to 30
start = int(input("enter the starting position:"))
end = int(input("enter the ending position:"))
def even():
    v = []
    for i in range(start,end):
        if i%2 == 0:
            v.append(i)
    print(v)
even()


#multiply all the numbers in list
# def mul(x):
#     num=1
#     for i in x:
#         #print(i)
#         num=num*i
#     return(num)
# j = [2,3,4]
# print(mul(j))


#factorial of a number
# n = int(input("enter the number:"))
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n))





