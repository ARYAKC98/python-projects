#defenition
def sum(a,b):
    return a+b
#print("a.add")    not mandatory
def sub(a,b):
    return a-b
#print("b.subtract")           not
def mul(a,b):
    return a*b
#print("c.multiply")            not
def div(a,b):
    return a/b
#print("d.divide")               not

#calling

operation = input("enter the operation: +,-,*,/ :")

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
if operation== '+':
    print(sum(num1,num2))
elif operation=='-':
    print(sub(num1,num2))
elif operation=='*':
    print(mul(num1,num2))
elif operation=="/":
    print(div(num1,num2))
else:
    print("invalid")