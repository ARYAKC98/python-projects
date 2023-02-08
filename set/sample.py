# set{}
# 1.immutable
# 2.unordered
# 3.unindexed
# 4.duplicates not allowed
# set items are unchangable,but you can remove items and add items


#set sample
# set1 = {1,2,3,4,5}
# print(set1)

a = {1,2,3,4,5}
b = {4,5,3,9,7}
#union
union = a|b
print("union is",union)

#intersection
intersec = a&b
print("intersection is",intersec)

#difference
diff = a-b
print("difference is",diff)

#symmetric difference
sym_diff = a^b
print("symmetric difference is",sym_diff)

