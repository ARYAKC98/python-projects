#fibanocci using range method
n = int(input("enter the num:"))
a,b=0,1
print("fibanocci series:")
print(a)
print(b)
for i in range(3,n+1):
    c = a+b
    print(c)
    a,b=b,c
