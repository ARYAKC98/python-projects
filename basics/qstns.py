#to check whether the given number is positive ,negative,or zero

# n = int(input("enter the number:"))
# if n>1:
#     print("the number is positive")
# elif n<1:
#     print("the number is negative")
# else:
#     print("number is zero")



#largest of three numbers using nested if
# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# c = int(input("enter the third number:"))
# if a>b:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# elif b>c:
#     print(b)
# else:
#     print(c)

#reverse of a number using while
n = 123   #123/10=Q=12,R=3
rev = 0
while n>0:                       #12>0,1>0
    r = n%10  #3,2,1
    rev = rev+r
    # rev = rev*10+r   #3,32,321
    n = n//10     #12,1
print("reverse of the num is",rev)


# #sum
# s=0
# s=s+r


# #product
# p=1
# p=p*r



# #check whether the entered number is palindrom or not
# n = int(input("enter the number:"))
# rev = 0
# temp = n
# while temp>0:
#     rem = temp%10
#     rev =rev*10+rem
#     temp = temp// 10
# if rev == n:
#     print("the num is palindrom")
# else:
#     print("the num is not palindrom")




