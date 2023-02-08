class A:
    def read(self):
        self.x = int(input("enter the 1st num:"))
        self.y = int(input("enter the 2nd num:"))
class B(A):
    def sum(self):
        print("the sum is",self.x+self.y)
class C(B):
    def avg(self):
        print("the average is",self.x+self.y/2)
ob = C()
ob.read()
ob.sum()
ob.avg()


