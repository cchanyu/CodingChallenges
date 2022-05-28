# Python Orject Oriented Programming
'''
Referenced video: Corey Schafer
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Property Decorater
'''

# LESSON 6

class Employee:

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    # we are defining it like a method, but accessing like an attribute
    # meaning you can just do emp_1.email, instead of emp_1.email()
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # this is a setter method, which allows you to change data
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first = None
        self.last = None

emp_1 = Employee("Chanyu", "Choung", 60000, 'python')
emp_2 = Employee("Karen", "Heaven", 65000, 'java')
emp_1.fullname = 'Corey Schafer'

print(emp_1.email())

# no need to add () with @property
print(emp_1.email)
print(emp_1.fullname)

# wipes emp_1's name
del emp_1.fullname