1 #print unique value in a dictionary -  [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

# listofdict = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# setof_uvalues = set()
# for i in listofdict:
#     for value in i.values():
#         setof_uvalues.add(value)
# print(setof_uvalues)

#OR

# dict = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# ul = []
# for i in dict:
#     ul.extend(list(i.values()))
# ul = set(ul)
# print(ul)


2 # combine values in python list of dictionaries - [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
d =[{'item':'item1','amount':400},
    {'item':'item2','amount':300},
    {'item':'item1','amount':750}]
lst = {}
for i in d:
    if i['item'] not in lst:
        lst[i['item']]=i['amount']
    else:
        lst[i['item']]+=i['amount']
print(lst)


3 #create a dictionary from a string
   #sample string:'Luminar'

# str1 = "Luminar"
# print(str1)
# dict={ }
# for i in range(1,(len(str1))+1):
#     dict.setdefault(i,str1[i-1])
# print(dict)



5# write a python program to print a dictionary in line by line
# dict = {'malayalam':98,'english':88,'maths':80,'science':90}
# for key,value in dict.items():
#     print(key, ' -- ',value)


#write a python program to sort(ascending and descending order) a dictionary by value
#{1:2,3:4,4:3,2:1,0:0}

# dict1 = {1:2,3:4,4:3,2:1,0:0}
# print("the given dictionary is : ",dict1,"\n")
# val = list(dict1.items())
# print(val)                     # create a list of tuples of key:value pairs
# newval = []
# newvalf = []
#
# for i in val:          #key:value pair
#     irev = i[::-1]             #ordering value:key format
#     newval.append(irev)        #appending value:key pairs to empty list
# print(newval)          #sorting based on values   value:key
#
# for i in newval:
#     irevf = i[::-1]                 #reversing whole value:key list back to key:value
#     val.append(irevf)               #appending to list
# # print(val,"/n")
#
# for i in (newval[::-1]):             #taking reverse of value:key list for taking descending order
#     i = i[::-1]                      #reversing back to key:value format
#     newvalf.append(i)                #appeending descending order pairs to list
# print(newvalf,"/n")
#
# print("the dictionary in ascending order of key value is:",dict(val),"\n")
# print("the dictionary is descending order is key value is:",dict(newvalf))
#


