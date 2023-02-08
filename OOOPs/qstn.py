"""find factorial of a number using class with function argument,return """

# class Emp:
#     def fact(self,n):
#         f=1
#         for i in range(1,n+1):
#             f=f*i
#         return  f
# obj = Emp()
# n = int(input("enter the num:"))
# f = obj.fact(n)
# print("factorial is:",f)
#


#using recursion
class Emp:
    def fact(sl,x):
        if x==1:
            return 1
        else:
            return x*sl.fact(x-1)
obj = Emp()
n = int(input("enter the num:"))
f = obj.fact(n)
print("factorial is",f)