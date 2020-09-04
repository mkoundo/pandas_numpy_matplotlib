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


class Developer(Employee):                          # Create Subclass - Developer class inherits from Employee class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)          # passes first, last and pay to the parent class, Employee
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # Methods to add, remove & print employees supervised by manager
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Joe', 'Blowe', 50000, 'python')
dev_2 = Developer('AN', 'Other', 60000, 'java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# isinstance shows is an instance of a given class
print(isinstance(mgr_1, Manager))           # True
print(isinstance(mgr_1, Employee))          # True
print(isinstance(mgr_1, Developer))         # False

# issubclass shows if a class is a subclass of given class
print(issubclass(Manager, Employee))           # True
print(issubclass(Developer, Employee))         # True
print(issubclass(Manager, Developer))          # False

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(help(Developer))                               # Shows method resolution order

# print(dev_1.email)
# print(dev_2.email)
#
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
