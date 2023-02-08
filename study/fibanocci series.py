n = int(input("enter the number:"))
a,b = 0,1
print("fibanocci series:")
print(a)
print(b)
for i in range(2+n):
    c = a+b
    print(c)
    a,b=b,c



