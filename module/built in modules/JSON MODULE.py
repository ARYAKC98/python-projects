# used to storing data and exchanging data
#inputs are in dictionary format
#json always in string format

# parse json - json to python
# json.loads


#import json
#print(dir(json))



import json
x = '{"name":"priya","age":12,"course":,"python"}'

# #parsing json to python
# y = json.loads(x)
# print(y)

#dumps to python
y = json.dumps(x)
print(y)
