# #sum
# add = lambda a,b:a+b
# print(add(2,5))


# #largest
# largest = lambda a,b:a if a>b else b
# print(largest(100,300))

#filter
l=[10,2,3,4,50,77,11]
lst = list(filter(lambda x:x%2==0,l))
print(lst)



# map
l = [10, 2, 3, 4, 50, 77, 11]
lst = list(map(lambda x: x%2 == 0, l))
print(lst)


# reduce
from functools import reduce
l1=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,l1)
print(product)