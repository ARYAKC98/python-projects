from mymodule import *
while True:
    opt=int(input('1.create\n2.search\n3.remove\n4.replace\n5.enter your choice'))
    if opt ==1:
       create()
    elif opt==2:
       search()
    elif opt==3:
        remove()
    elif opt==4:
        replace()
    else:
        break
