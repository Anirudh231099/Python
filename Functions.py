class Employee:
    'id,name,city'

    def details(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

    def print(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("City:", self.city)

def employee():
    emp = Employee()
    emp.details(1, 'Anirudh', 'Bangalore')
    emp.print()

employee()



# class Employee:
#     def __init__(self, name,designation,city):
#         self.name = name
#         self.designation = designation
#         self.city = city
#
#     def details(self):
#         print("Employee Name:", self.name)
#         print("Employee Designation:", self.designation)
#         print("Employee City :", self.city)
#
#
# emp = Employee("Anirudh", "Associate Consultant","Bangalore")
# emp.details()



# class Student:
#   def __init__(self, name, age,course):
#     self.name = name
#     self.age = age
#     self.course=course
#
# s1 = Student("Anirudh", 21,"CSE")
#
# print(s1.name)
# print(s1.age)
# print(s1.course)



# class Dog:
#    # class attribute
#    a='Global'
#    # Instance attribute
#    def __init__(self, name): #DEFAULT CONSTRUCTOR
#       self.name = name
#       self.attr1 = "Boy"
#       print(self.attr1)
#    def speak(self):
#       print("My name is {}".format(self.name))
#       print(self.attr1)
# # Driver code
# # Object instantiation #DOG D("JANCY");
# J = Dog("JANCY") #SELF-->REPRESNTS THE INSTANCE
# T = Dog("Tom")
# # Accessing class attributes
# print("John is a {}".format(J.__class__.a))
# print("Tom is also a {}".format(T.__class__.a))
# # Accessing instance attributes
# print("My name is {} ... How are you  {}".format(J.name,J.name))
# print("My name is {}".format(T.name))
# # Accessing class methods
# J.speak()
# T.speak()
#






# class Dog:
#    # class attribute
#    a='Global'
#    # Instance attribute
#    def __init__(self, name): #DEFAULT CONSTRUCTOR
#       self.name = name
#       self.attr1 = "Boy"
#       print(self.attr1)
#    def speak(self):
#       print("My name is {}".format(self.name))
#       print(self.attr1)
# # Driver code
# # Object instantiation #DOG D("JANCY");
# J = Dog("JANCY") #SELF-->REPRESNTS THE INSTANCE
# T = Dog("Tom")
# # Accessing class attributes
# print("John is a {}".format(J.__class__.a))
# print("Tom is also a {}".format(T.__class__.a))
# # Accessing instance attributes
# print("My name is {} ... How are you  {}".format(J.name,J.name))
# print("My name is {}".format(T.name))
# # Accessing class methods
# J.speak()
# T.speak()
#
