class Base:
    def __init__(self):
        self.a = "komal"
        self.__c = "papaniya"
        # print(self.__c)
  
# Creating a derived class
class Derive(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # print(self.__c)
  
  
# Driver code
obj1 = Base()
o = Derive()
print(8)