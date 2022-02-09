# #Base Class
# class User:
#
#    def getinfo(self):
#      print("Learn Python")
#
# #Derived Class
# class Employees(User):
#
#    def getinfo(self):
#      print("Welcome to Python")
#
# e1 = Employees()
# e1.getinfo()


class Animal:
    def Walk(self):
        print('Hello, I am the parent class')

class Dog(Animal):
    def Walk(self):
        print('Hello, I am the child class')

print('The method Walk here is overridden ')

r = Dog()
r.Walk()

r = Animal()
r.Walk()