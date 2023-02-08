n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        ch = chr(64+i)

        if (i==1 or i==n or j==1 or j==n):
            print(ch,end=" ")
        else:
            print(' ',end=' ')
    print(' ')



n = int(input("enter the num:"))
for i in range(n):
    for j in range(n+1):
        if j==0 or i==(n+1) or i==j:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()