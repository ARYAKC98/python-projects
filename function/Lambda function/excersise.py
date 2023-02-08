"""write a python programme to create a function that takes one argument and that argument will be multiplied with a
    unknown given number"""

def func(n):
    return lambda a: a * n
myfunc = func(5)
print(myfunc(2))

"""write a programme to  filter a list of integers using lambda"""

# print even numbers in a list using lambda filter
num = [1,2,3,4,5,6]
even_num = list(filter(lambda a: a%2==0,num))
print(even_num)

#print odd numbers
num = [1,2,3,4,5,6,7,8]
odd_num = list(filter(lambda a: a%2==1,num))
print(odd_num)


#lambda with if else condition
max = lambda a,b : a if a>b else b
print(max(4,6))

maxim = lambda a,b,c: a if(a>b and a>c) else b if(b>a and b>c) else c
print(maxim(4,6,9))

#map function    (maping of two objects)
"""map function is used to execute a function for each element in an iterable"""
def my_func(a,b):
    return a+b

x = map(my_func,("apple","orange","mango"),("cherry","banana","pineapple"))
print(list(x))


#reduce (code resduction)


