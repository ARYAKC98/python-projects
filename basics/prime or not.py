n = int(input("enter the num:"))
f = 0
#n=5----5%1=0,5%2=1,5%3=2,5%4=3,5%5=0
if n==1:
    print("not defined:")
else:
    for i in range(1,n+1):#1---n
        if n%i==0:
            f=f+1 #2
    if f==2:
        print("prime")
    else:
        print("not prime")



#break statement
# l = [10,20,30,50,100,60,70,80]
# for x in l:
#     print(x)
#     if x==100:
#         break


#continue statement
# l = [10,20,30,50,100,60,70,80]
# for x in l:
#     if x==100:
#         continue
#     print(x)


