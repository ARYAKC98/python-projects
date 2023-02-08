#reduce code size in an already existing list
#list comprehension can be used in multiple loops and multiple conditions

lst = ["banana","mango","apple","cherry"]
new_lst = [x for x in lst if 'a' in x]
print(new_lst)


#multiple loops
prime = [x for x in range(2,21) if all(x%y!=0 for y in range(2,x))]
print(prime)

#multiple condition
num_lst = [y for y in range(100) if y%2==0 if y%5==0]
print(num_lst)


#find even
even = [ x for x in range(100) if x%2==0]
print(even)

#find odd
odd = [x for x in range(100) if x%2!=0]
print(odd)