# Python Orject Oriented Programming
'''
Referenced video: Corey Schafer
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Creating a simple class and instances of simple class.
Initialize the class attribute and create methods.
'''

# LESSON 1

class Employee:

    # initialization - meaning creation of an instance
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    # function - it does something using the specified instance.
    def fullname(self):
        return "{} {}".format(self.first, self.last)

# These creates the instances of new Employee
emp_1 = Employee("Chanyu", "Choung", 60000)
emp_2 = Employee("Karen", "Heaven", 65000)

# emp_1.fullname - prints the method
# emp_1.fullname - prints the return value of method
print(emp_1.fullname())
print(emp_2.fullname())

# These do the same, 
# emp_1.fullname() actually gets transformed to the 2nd line behind the scene.
'''
emp_1.fullname()
Employee.fullname(emp_1)
'''

# this is not OOP, this is manually creating, which we want to avoid
'''
emp_1.first = "Chanyu"
emp_1.last = "Choung"
emp_1.email = "CC@gmail.com"
emp_1.pay = 60000

emp_1.first = "Karen"
emp_1.last = "Heaven"
emp_1.email = "KH@gmail.com"
emp_1.pay = 65000

print(emp_1.email)
print(emp_2.email)

print("{} {}".format(emp_1.first, emp_2.last))
'''