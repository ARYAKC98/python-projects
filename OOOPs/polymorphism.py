# #1.compile time (eg:function overloading)
# #2.runtime time (eg:function overriding)
# class A:
#     def display(selfself,name=None):
#         if name is None:
#             print('hello')
#         else:
#             print('hello'+name)
# ob=A()
# ob.display()
# ob.display('anu')



#overriding
class rectangle():
    def Area(self,l,b):
        print("area of rectangle is:",l*b)

class square(rectangle):
    def Area(self,l,b):
        print("area of square is:",l*b)
ob=square()
ob.Area(10,20)
