""'accessmodifier"""

#super class
class A:
    #public data member
    var1 = None

    #protected data member
    _var2 = None

    #private data member
    __var3 = None


    #constructor
    def __init__(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3


    #public member function
    def displaypublicmembers(self):
        #accessing public data members
        print("public data member:",self.var1)

    #protected member function
    def _displayprotectedmembers(self):
        #accessing protected data members
        print("protected data members:",self._var2)

    #private member function
    def __displayprivatemembers(self):
        #accessing private data members
        print("private data member:",self.__var3)

        # public member function
    def accessprivatemembers(self):
         #accessing private member function
        self.__displayprivatemembers()




#derived class
class B(A):

    #constructor
    def __init__(self,var1,var2,var3):
        A.__init__(self,var1,var2,var3)


    #public member function
    def accessprotectedmembers(self):
        # accessing protected member function of super class
        self._displayprotectedmembers()


#creating objects of derived class
obj = B("pub_red","pro_white","private_green")

#calling public member functions of the class
obj.displaypublicmembers()
obj.accessprotectedmembers()
obj.accessprivatemembers()
#obj.accessprivatemembers()
#object can access public member
print("object is accessing public member:",obj.var1)
#object can access protected member
print("object is accessing protected member:",obj._var2)


#object cannot access private member,so it will generate atribute error
#print (obj.__var3)
print(obj._A__var3)#accessing name mangled variables
#name mangling
#a process in which any given identifier with one trailing underscore and two leading underscores
#is textually replaced with the _classname__identifier is known as name mangling
# in _classname__identifier name,classname is the current class where identifier is present