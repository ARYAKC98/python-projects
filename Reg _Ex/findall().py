#findall()
import re
str = "rose is a beautiful and colourful flower"
s = re.findall('ful',str)
print(s)



s1 = re.findall('full',str)
print(s1)



d='cat mat pat rat sat'
a=re.findall('[scr]at',d)
print(a)



d='cat mat pat rat sat'
a=re.findall('^[scr]at',d)
print(a)

d='cat mat pat rat sat 99988  999 6666'
a = re.findall('\d{3}',d)
print(a)


d='cat mat pat rat sat 99988  999 6666'
a = re.findall('\d{1,4}',d)
print(a)




d='cat mat pat rat sat 99988  9999 6666'
a = re.findall(r'\b\d{4}\b',d)
print(a)
