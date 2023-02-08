#reverse a tuple
# tple = (1,2,3,4)
# reverse = tple[::-1]
# print(reverse)



#tple = (1,2,40,30,20)   to access the value from the tuple
# tple = (1,2,40,30,20)
# a = tple[4]
# print(a)





#tple = (1,2,40,30,20)  tple = (1,2,40,[10,2,30],(30,20,10),40)
# to access the value from the tuple
#to remove repeated elements from this tuple

# tple1 = (1,2,40,30,20)
# y = tple1[4]
# print(y)
# tple2 =  (1,2,40,[10,2,30],(30,20,10),40)
# a = tple2[4][1]
# print(a)

#remove
tple2 =  (1,2,40,[10,2,30],(30,20,10),40)
list1= list(tple2)
# print(list1)
for i in list1:
    x=list1.count(i)
    if x>1:
        list1.remove(i)
print(list1)





#check if all items in the tuple are same
#copy specific elements from one tuple to a new tuple
tple1 = (1,3,5,6,3)
tple2 = tple1[2]
print(tple2)








#swap two tuples in python


