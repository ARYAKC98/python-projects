#write a python program to convert a string  to tuple
# str = "hello madam"
# tple = tuple(str)
# print(tple)




#write a python program to convert a list to a tuple
# my_list = [1,2,3,4]
# tple = tuple(my_list)
# print(tple)




#write a python program to find repeated items from a tuple
# tple = (1,2,"world",2,6,2)
# tuple = tple.count(2)
# print(tuple)


#check if all items in the tuple are same
tup = (1,1,1,1,1)
tple = set(tup)
if len(tple) == 1:
    print("same")
else:
    print("not same")



#method2
# tup = (1,1,1,1,1)
# f = 1
# for i in tup:
#     for j in range(i,len(tup)-1):
#         if tup[i] != tup[j+i]:
#             f=0
#             break
# if f == 1:
#     print("same")
# else:
#     print("not same")