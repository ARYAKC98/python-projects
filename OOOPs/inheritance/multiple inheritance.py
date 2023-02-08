class A:
    def employee(self):
        self.x=input('enter the name:')
        self.y= input('enter age:')
class B:
    def salary(self):
        self.a=input("first month salary:")
        self.b=input("second month salary:")
class C(A,B):
    def display(self):
        print("{}:{}:{}:{}:{}".format("name is:",self.x,"age is:",self.y,"nov salary:",self.a,"dec salary",self.b))
ob=C()
ob.employee()
ob.salary()
