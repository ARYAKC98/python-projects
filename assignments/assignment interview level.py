#write a code to reverse a number

n=int(input("enter the number :"))
reverse = 0
while n>0 :
    reminder = n%10
    reverse = reverse*10+reminder
    n = int(n/10)
print(reverse)


#palindrom or not

str = input("enter a string:")
if (str==str[::-1]):
    print("the string is a palindrome")
else:
    print("not a palindrome")
