import random
#print(dir(random))
y = random.random()
print(y)


#randint
y = random.randint(1,100)
print(y)

#randrange()
x = random.randrange(1,10,2)
print(x)

#choice()
y = random.choice("hello")
print(y)


#shuffle
num = [1,2,3,4,5,6]
y = random.shuffle(num)
print(num)