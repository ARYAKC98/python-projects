def prime(x):
    if x ==1 :
        print("1 is neither prime or composite")
    elif x<1:
        print("the number is negative")
    elif x==2:
        print("number is prime value")
    else:
        flag=1
        for j in range(2,x):
            if x%j == 0:
                flag=0
                break
            else:
                continue
        if flag == 0:
            print(f"the number{x} is not prime")
        else:
            print(f"the number {x} is primee")
num = int(input("enter any number:"))
prime(num)