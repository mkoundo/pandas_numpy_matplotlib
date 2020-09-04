# Python Object-Orientated Programming

class Employee:                                     # Define a class

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first                          # Instance Variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):                             # A regular method automatically passes the instance as the first argument, which we call self
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Magic or Dunder (double underscore) method

    # replaces object at memory gibberish with something more readable
    # print(emp_1)  ---> <__main__.Employee object at 0x000002843A4F7400>
    # str takes precedence over repr when you print
    def __repr__(self):                             # used for debugging - to be displayed to devs only
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):                              # used to display to end users
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Joe', 'Blowe', 50000)
emp_2 = Employee('AN', 'Other', 60000)


print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1 + emp_2)

print(len('test'))
print('test'.__len__())

print(emp_1.fullname())
print(len(emp_1))
