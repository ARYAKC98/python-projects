"""read method"""
# f=open('test1.py','r')
# print(f.read())

# print(f.readline(8))

# print(f.readline())
# print(f.readline())



# f=open('test1.py','r')
# for i in f:
#     print(i)
# f.close()




# """append method"""
# f=open('test1.py','a')
# f.write('python is a oops')
# f.close()



# """write"""
# f=open('test1.py','w')
# f.write('python is a oops')
# f.close()



# """seek()"""  current file position set
# """file.seek(offset)"""
#
# f=open('test1.py','r')
# f.seek(8)
# print(f.readline())
# f.close()


# """tell()"""  current file position get
# """fileobject.tell()"""
# f=open('test1.py','r')
# f.readline()
# pos=f.tell()
# f.close()
# print('position is:',pos)




# """write a prgrm to read a file line by line and store in to a list"""
# def file_read(fna):
#     with open(fna) as f:
#         output_list=f.readlines()
#     print(output_list)
# file_read('test1')


# from shutil import copyfile
# copyfile('test1','test2')

# qstn
str='cat rat mat cat pat rat cat sat cat sat'
print(str)
lst=str.split(' ')
print(lst)
d={}
for i in lst:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)











