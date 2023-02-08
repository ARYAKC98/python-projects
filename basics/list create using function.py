l = []
def create():
    limit=int(input("enter the limit:"))
    for i in range(limit):
        item =int(input("enter the item:"))
        l.append(item)
    print(l)
create()

#
# #search
def search():
    item = int(input("enter the item to search:"))
    if item in l:
        print("item found")
    else:
        print("item not found")
search()
#
# #remove
def remove():
    item = int(input("enter the item to remove:"))
    if item in l:
        l.remove(item)
    else:
        print("not found in l")
    print(l)
remove()


#replace
def replace():
    old = int(input("enter the item to be replaced:"))
    new = int(input("enter the new item replaced:"))
    for i in range(len(l)):
        if l[i]==old:
            l[i]=new
    print(l)
replace()




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
