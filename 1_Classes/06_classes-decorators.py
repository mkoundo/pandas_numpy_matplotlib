# Python Object-Orientated Programming
# Getters, Setters and Deleters

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Add property decorator
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# Suppose you want to update the first name of emp_1
# the problem is that the email still shows the old first name
# emp_1.first = 'Jim'

emp_1.fullname = 'Joe Blowe'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

