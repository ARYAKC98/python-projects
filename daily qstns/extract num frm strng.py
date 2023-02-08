"""write a program to extract numbers from a string by using list comprehension"""

str1 = "the room number 45 and 67 are vacant"
new_str=[x for x in str1 if x.isdigit()]
print(new_str)