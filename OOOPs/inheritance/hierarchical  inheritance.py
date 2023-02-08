class A:
    def read(self):
        self.x = int(input("enter the 1st num:"))
        self.y = int(input("enter the 2nd num:"))
class B(A):
    def sum(self):
        print("sum is",self.x+self.y)
class C(A):
    def avg(self):
        print("avg is",(self.x+self.y)/2)
class D(A):
    def product(self):
        print("the product is",self.x*self.y)

ob1=B()
ob1.read()
ob1.sum()
ob2=C()
ob2.read()
ob2.avg()
ob3=D()
ob3.read()
ob3.product()