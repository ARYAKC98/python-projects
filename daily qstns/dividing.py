"""WAP prgrm to print all numbers in a range divisble by a given number"""

lower = int(input("enter lower range limit:"))
upper = int(input("enter upper range limit:"))
n = int(input("enter the number to be divided by :"))
#the reminder of the number divided by i is eqaual to 0, i is printed
for i in range(lower,upper +1):
    if(i%n==0):
        print(i)