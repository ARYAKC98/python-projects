"""write a python program to get generate a random colour hex,a random alphabetical string,random value between two integiers,
  and random multiple of 7 between 0 and 70.
   hint:use random.randint()"""

import random
#rand=random.randint(0,16777215)
hex_num = str(hex())

#string
print(random.choice("welcome"))
#
print(random.randrange(0,70,7))

print(random.randrange(1,80))