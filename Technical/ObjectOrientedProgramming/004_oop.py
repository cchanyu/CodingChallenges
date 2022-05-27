# Python Orject Oriented Programming
'''
Referenced video: Corey Schafer
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Inheritance - inherit attributes from a parent class
'''

# LESSON 4

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

# just by inheriting, it has access to all the instances and methods of the parent class
# meaning it can use anything from Employee functions as well.
class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay) # super inherits parent's first, last, pay
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay) # super inherits parent's first, last, pay
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


# Despite Developer class being empty, it's capable of creating this instances.
# This is called Method Resolution Order - it's searching parent's class for what it's looking for, cause child class doesn't have it.
dev_1 = Developer("Chanyu", "Choung", 60000, 'python')
dev_2 = Developer("Karen", "Heaven", 65000, 'java')

# this prints out Method Resolution Order
# it shows the order where python is looking for.
'''print(help(Developer))'''
print(dev_1.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager)) # checks whether mgr_1 is an instance of Manager
print(isinstance(mgr_1, Employee)) # also true, cause it's parent inheritance
print(issubclass(Manager, Employee)) # checks the subclass