# Python Object-Orientated Programming


class Employee:                                     # Define a class

    num_of_emps = 0                                 # Class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first                          # Instance Variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'email.com'

        Employee.num_of_emps += 1

    def fullname(self):                             # Create a method
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Joe', 'Blowe', 50000)             # Create a class instance
emp_2 = Employee('AN', 'Other', 60000)

print(Employee.num_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
# print(Employee.__dict__)
