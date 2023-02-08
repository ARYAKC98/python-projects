n = int(input("enter the year:"))
#divided by 100 means century year (ending 00)
#century year divided by 400 is leap year
if (n%400==0) and (n%100==0):
    print(n,"is leap year")

#not divided by 100 means not a century year
#year divided by 4 is a leap year

elif (n%4==0) and (n%100!=0):
    print(n, "is a leap year")

else:
    print(n, "is not a leap year")