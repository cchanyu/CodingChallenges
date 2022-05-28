# Python Orject Oriented Programming
'''
Referenced video: Corey Schafer
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Special (Magic/Dunder) Methods
'''

# LESSON 5

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # Dunder init, it's talking about this -> '__ __'
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

    @classmethod
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
    
    # representation
    # meant be to unambigious representation of an object, used for debugging and seen by other devs.
    def __repr__(self) -> str:
        return ("Employee('{}', '{}', '{}'".format(self.first, self.last, self.pay))

    # string
    # readable representation for an object and used to display info for end users
    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer("Chanyu", "Choung", 60000, 'python')
dev_2 = Developer("Karen", "Heaven", 65000, 'java')

print(emp_1)
# These directly call those special methods
print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

# dunder add can also be directly accessed
print(1+2)
print(int.__add__(1,2))
print(str.__add__('a', 'b')) # str dunder add concats together: ab

# these use dunder add we made in the obj and adds their salary together
print(emp_1 + emp_2)

# python documentation on dunder numeric types (3.3.7)
# https://docs.python.org/3/reference/datamodel.html

print(len('test'))
print('test'.__len__())
print(len(emp_1))
