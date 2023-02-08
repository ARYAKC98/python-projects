#OOPs - program are based on class and object
#class - class is the way to bind functions and its related data
#object - instance of a class or runtime entity of a class


# #function
# def sum():
#     a,b=10,20
#     s = a+b
#     return s
# s1=sum()
# print("sum is:",s1)


#function parameter
# def sum(x,y):
#     s = x+y
#     return s
# s1=sum(100,200)
# print("sum is:",s1)



#wap to find factorial of a number using function with return type and parameter
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# f1 = fact(5)
# print("factorial is:",f1)


#
# #arbitary argument
# def colour(*args):
#     #print(args[0])
#     for i in args:
#         print(i)
# colour('red','white','pink')

# #keyword arguments
# def stud(st1,st2,st3):
#     print('first:',st1)
#     print('second:',st2)
#     print('third:',st3)
# stud(st2='anu',st3='maya',st1='krishna')



# def stud(**kwargs):
#     for i,j in kwargs.items():
#         print('%s=>%s'%(i,j))
# stud(st2='anu',st3='maya',st1='krishna')



# #combination of three arguments
# def student(x,*args,**kwargs):
#     print('simple argument:',x)
#     for j in args:
#         print(j)
#     for i,j in kwargs.items():
#         print('%s=>%s'%(i,j))
#
# student('amal','varun','sini',st2='anu',st1='kiran',st3='arun')


# #default parameter value
# def display(country='india'):
#     print('i am from',country)
# display()
# display('america')



##list
def dis(ls):
    for i in ls:
        print(i)
dis([10,20,30])







