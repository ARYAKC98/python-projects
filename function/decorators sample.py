# def upper_decor(fun):
#     def wrapper():
#         result = fun()
#         return result.upper()
#     return wrapper()
#
# def hello_name():
#     return "hello"
# f = upper_decor(hello_name)
# print(f)


#using decorator
def upper_decor(fun):
    def wrapper(name):
        result=fun(name)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return"hello"+name
print(hello_name(" arya"))