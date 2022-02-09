# ---------------------------------PROTECTED----------------------------------------------

# class Base:
#     def __init__(self):
#         # Protected member with _ (underscore)
#         self._age = 22
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ",self._age)
#
#         # Modify the protected variable:
#         self._age = 23
#         print("Calling modified protected member outside class: ",self._age)
#
# obj1 = Derived()
# obj2 = Base()
#
# # Calling protected member
# print("Accessing protected member of obj1: ", obj1._age)
# print("Accessing protected member of obj2: ", obj2._age)


#--------------------------------------- PRIVATE-------------------------------------------

# class Base:
#     def __init__(self):
#         self.a = "Anirudh"
#         self.__c = "Private"
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
#
# obj1 = Base()
# print(obj1.a)
# # obj2 = Derived()
# # print(obj2.a)


# --------------------------------Public---------------------------------------------------

class public:

    # constructor
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def display(self):
        print("Name: ", obj.Name)
        print("Age: ", self.Age)


obj = public("Anirudh", 20)
obj.display()
