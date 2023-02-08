#factorial of a number
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
f = fact(5)
print(f)