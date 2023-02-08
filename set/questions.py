# 1.add a list of elements to a set

# 2.get only unique items from two sets

# 3.check if two sets have any elements in common .if yes ,display the common elements

# 4.remove items from set1 that are not common of both set1 and set2
#        set1 = {10,20,30,40,50}
#        set2 = {30,40,50,60,70
#    exp o/p = {40,50,30}



#1
# set1 = {1,2,3,4}
# list = [5,6,7,8]
# set1.update(list)        #update- |=   update used to adding elements from iterable or another set
# print(set1)

#2
# set1 ={10,20,30,40}
# set2 ={60,40,70,20}
# unique = set1|set2   #using union ..it prints all uncommon elements.....union is correct method here
# #unique = set1^set2    #using symmetric difference,print only unique items
# print(unique)



#3
# set1 = {10,20,30,40,50}
# set2 = {40,50,60,70,80}
#
# if set1.isdisjoint(set2):
#     print("two sets have no items in common")
# else:
#     print("two sets have items in common")
#     print(set1.intersection(set2))


#4
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
#print(set1&set2)
set1.intersection_update(set2)        #remove the items that not present in both sets
print(set1)








