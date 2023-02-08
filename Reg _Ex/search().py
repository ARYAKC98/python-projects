import re
# str ='class will start at 10am'
# s=re.search('\s',str)
# print(s)
# print(s.start())
#
#
#
# s1=re.search('\d',str)
# print(s1.start())
#
#
# s2 = re.search('python',str)
# print(s2)
#
#
# str='class will start at 10am'
# print(s)
# if s:
#     print("find")
# else:
#     print("not find")



str='class will start at 10am'
s=re.search('^class.*10am$',str)
print(s)
if s:
    print("find")
else:
    print("not find")