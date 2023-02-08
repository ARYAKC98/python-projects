"""Filter the array, and return a new array with only the values equal to or above 18"""

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:                                 #or print(list(adults))
  print(x)

