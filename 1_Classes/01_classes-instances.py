# Python Object-Orientated Programming


class Employee:                                     # Define a class
    def __init__(self, first, last, pay):
        self.first = first                          # Initialise class attributes
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'email.com'

    def fullname(self):                             # Create a method
        return f'{self.first} {self.last}'


emp_1 = Employee('Joe', 'Blowe', 50000)             # Create a class instance
emp_2 = Employee('AN', 'Other', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# print(f'{emp_1.first} {emp_1.last}')
print(emp_1.fullname())                 # use () for methods
print(emp_2.fullname())
# OR
print(Employee.fullname(emp_1))
