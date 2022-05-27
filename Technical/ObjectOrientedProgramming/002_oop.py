# Python Orject Oriented Programming
'''
Referenced video: Corey Schafer
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Class variables - a variable contained within class.
It's not instance variable, where variables are kept inside of instances.
'''

# LESSON 2

class Employee:

    # these are class variables
    num_of_emps = 0
    raise_amount = 1.04

    # variables inside of this is instance variables
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Chanyu", "Choung", 60000)
emp_2 = Employee("Karen", "Heaven", 65000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

'''
Class variable example:
Employees get raised pay every year and it's all equal.

emp_1.raise_amount = 1.05

Employee.raise_amount - globally change
self.raise_amount - changes for specific instance only
'''