 # class Emp:
#     def display(self):
#         print("simple function")
# obj = Emp()                 #object name= class name
# obj.display()


#rare case
# class Emp:
#      x= 100
#      def display(self):
#          print("simple function")
#      def disp():
#         print("without self parameter")
# obj = Emp()
# obj.display()
# print("value of x is",obj.x)
# ob = Emp
# ob.disp()


#with arguments
# class Emp:
#     x = 100
#     def display(self):
#         print('simple function')
#     def sum(self,a,b):
#         print('sum is',a+b)
#     def product(self,a,b):
#         print('product is',a*b)
# obj = Emp()
# obj.display()
# obj.sum(30,60)
# obj.product(3,5)





# class Emp:
#     def read(self,a,b):
#         self.x=a
#         self.y=b
#     def sum(self):
#         print('sum is',self.x+self.y)
#     def product(c):
#         print('the product is',c.x*c.y)
# obj = Emp()
# obj.read(30,40)
# obj.sum()
# obj.product()




class Emp:
    def read(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print('sum is',self.a+self.a)
    def product(c):
        print('the product is',c.b*c.b)
obj = Emp()
obj.read(30,40)
obj.sum()
obj.product()