# #1.non paraameterized constructor
#
# #EG:
# class A:
#     def __init__(self):
#         print("non parameterized constructor")
# ob = A()



# #parameterized constructor
# class A:
#     def __init__(self,name):
#         print("parameterized constructor")
#         self.na=name
#     def display(self):
#         print("name is:",self.na)
#
# obj = A('maya') 
# obj.display()

#destructor
class A:
    def __init__(self,name):
        print("parameterized constructor")
        self.na=name
    # def __del__(self):
    #     print("destructors")
    def display(self):
        print("name is:",self.na)

obj = A('maya')
del obj
#obj.display()

