"""write a program to print the strings that start with the letter 'c' and end with the letter 'b'"""

names=['chb','ydb','thd','hgt','cqyb']
new_name =[name for name in names if name.endswith('b')&name.startswith('c')]
print(new_name)