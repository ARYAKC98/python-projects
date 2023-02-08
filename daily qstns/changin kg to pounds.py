"""changing from kilogram to pound using list comprehension"""

old_weight = {
    'book':0.5,
    'milk':2.0,
    'tv':7.0
}
new_weight={key : value*2.2 for (key,value)in old_weight.items()}
print(new_weight)