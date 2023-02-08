# str1 = ["John"," ","Jack","Emma"," ","Jins","Lina"]
# while ' ' in str1:
#     str1.remove(' ')
# print(str1)




str = "let’s google the pineapple"
str1 = str.split(' ')
print(str1)
str2 = []
print(str2)
for i in str1:
    l = " "
    for j in l:
       print(j)
    if j in l:
            continue
    else:
        l = l+j
        print(l)
    str2.append(l)
print(' '.join(str2))
