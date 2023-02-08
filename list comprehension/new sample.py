# syntax = list[expression for item in list if condition]

# l=[x+3 for x in [1,2,3]]
# print(l)
#
#
# #even
# l = [i for i in range(25)  if i%2==0]
# print(l)
#
#
# #return vowels from a string
# l = [i for i in 'hai mommy' if i in ['a','e','i','o','u']]
# print(l)
#
#
# #using split method take words first letter
# str = "hai how are you"
# str1 = str.split( )
# print(str1)
# l = [i[0] for i in str1]
# print(l)

# # only print a particular spelling included word
# colors=['red','white','green','pink']
# l = [i for i in colors if 'e' in i]
# print(l)

# #remove one word
# colors=['red','white','green','pink']
# l = [i for i in colors if i!='green']
# print(l)


# #upper
# colors=['red','white','green','pink']
# l = [i.upper() for i in colors]
# print(l)


# colors=['red','white','green','pink']
# l =['hello' for i in colors]
# print(l)



colors=['red','white','green','pink']
newlist=[i if i!='pink' else 'blue' for i in colors]
print(newlist)