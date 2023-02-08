# tple = (1,2,3,4,"haii")
# print(tple)

# list to tuple
# tple = [1,2,3,4,"hello",88]
# print(tuple(tple))

# nested tuple   (just checking nested tuple is allowed?)
# tple = ((19.29),"haii",[1,2,3],"madam")
# print(tple)


# slicing
# tple = (1,2,3,4,"haii",2.5)
# print(tple[:-1])

# print(tple[0])
#
# print(tple[::-1])
#
# print(tple[0:3])
#
# print(tple[-4:-1])
#
# print(tple[2])



# update/replace      (first convert into list..bcz tuple is immutable)
# tple = (1,"arya","athul","rahul",2,3,4,"haii",2.5)
# y = list(tple)                    #mutable data type
# y[0] = "dona"
# tple = tuple(y)
# print(tple)



#append           (convert in to list)        (in append added the value at last position)
# tple = (1,"arya","athul","rahul",2,3,4,"haii",2.5)
# y = list(tple)
# y.append("malayalam")
# tple = tuple(y)
# print(tple)



#nested tuple       (concantenating using nested tuple)
# tple = (1,"arya","athul","rahul",2,3,4,"haii",2.5)
# a = ("haii",(1,2,3))
# tple += a
# print(tple)





#remove               (convert into list)
# tple = (1,"arya","athul","rahul",2,3,4,"haii",2.5)
# y = list(tple)
# y.remove("haii")
# tple=tuple(y)
# print(tple)


#del                    (can't delete only one..bcz tuple is immutable...we can delete all the values)
# new_tuple = (1,"arya","athul","rahul",2,3,4,"haii",2.5)
# del new_tuple
# print(new_tuple)


#packing  (accessing values to  variable
# fruits = ("apple","cherry","strawberry","mango")
# (green,*red,yellow) = fruits
# print(green)
# print(red)
# print(yellow)


#while loop
# this_tuple = ("apple","banana","orange")
# i = 0
# while i<(len(this_tuple)):
#     print(this_tuple[i])
#     i = i+1


#nested tuple indexing
# n_tuple = ("sreya",[8,4,6],(1,2,3))
# # print(n_tuple)
# n_tuple[1][1]=23
# print(n_tuple)



#any()
#all()
#max()
#min()
#sorted()
#len()
#sum()

# a = (1,2,3,6,4,5)
# print(any(a))
#
# print(all(a))

# print(max(a))
#
# print(min(a))
#
# print(len(a))
#
# print(sum(a))



#enumerate  zip    (it can be used in any data type)(enumerate used to print index no)
names = ["mukesh","roni","cherry"]
ages = [24,43,34]
for i,(name,age)in enumerate(zip(names,ages)):            #(zip is used to print corresponding name and age)
    print(i,name,age)



#enumerate list to  tuple
names = ["mukesh","roni","cherry"]
ages = [24,43,34]
tple1 = tuple(names)
print(tple1)
tple2 = tuple(ages)
print(tple2)



#another enumerate program
letters = [('a','A'),('b','B')]
for i,letters in enumerate(letters):
    print("letters %d is %s/%s" %(i,letters[0],letters[1]))


#enumerate map
l = [('sat','cat','mat')]
test = list(map(list,l))
print(test)