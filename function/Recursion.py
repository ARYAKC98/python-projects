#factorail
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)              #5*fact(5-1)=[4]
print(fact(5))                          #5*4*fact(3)
                                        #5*4*3*fact(2)
                                        #5*4*3*2*fact(1)
                                        #5*4*3*2*1

#sum of n natural numbers
def sum(n):
    if n== 0:
        return 1
    else:
        return n*(n+1)/2
print(sum(16))