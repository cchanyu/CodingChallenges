# Python Orject Oriented Programming
'''
Referenced video: Corey Schafer
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Class Methods vs. Static Methods
Class methods - alternative constructor
Static methods - don't operate for instances or class
'''

# LESSON 3

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

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

    # class method affects the whole class
    @classmethod # this is decorater - altering the functionality of method
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Chanyu", "Choung", 60000)
emp_2 = Employee("Karen", "Heaven", 65000)


'''
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05) # this still changes all of the instance amounts
'''

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-80000'
emp_str_3 = 'Jane-Doe-75000'

'''
first, last, pay = emp_str_1.split('-') # splits string into first, last, pay
new_emp_1 = Employee(first, last, pay)
'''

# instead of 2 of commands above, this does it at one go
new_emp_1 = Employee.from_string(emp_str_1)

# regular methods automatically passes instance (SELF)
# class method pass class (CLS)
# static method doesn't pass anything

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))