class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True

emp = Person("Rahul")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Rishab")  # An Object of Employee
print(emp.getName(), emp.isEmployee())