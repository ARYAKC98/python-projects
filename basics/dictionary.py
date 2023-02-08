#update
# student = {"name:maya","course:python"}
# print(student)
# student.update({"batch":"december"})
# print(student)

#another method
# d = {}
# n = int(input('enter the number of elements in the dictionary:'))
# for i in range(n):
#     key = int(input('enter the key:'))
#     value=(input('enter the value:'))
#     d.update({key:value})
# print(d)



#only take key
d = {1:"red",2:"yellow"}
for i in d.keys():
    print(i)

#take value
for i in d.values():
    print(i)

for i,j in d.items():
    print(i,j)


#get()
x = d.get(2)
print(x)