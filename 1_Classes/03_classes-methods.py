# Python Object-Orientated Programming
import datetime


class Employee:                                     # Define a class

    num_of_emps = 0                                 # Class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first                          # Instance Variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):                             # A regular method automatically passes the instance as the first argument, which we call self
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod                                    # decorator
    def set_raise_amt(cls, amount):                 # A class method automatically passes the class as the first argument, which is called cls
        cls.raise_amount = amount

    @classmethod                                    # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):                            # Static method doesn't pass instance or class
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Joe', 'Blowe', 50000)             # Create a class instance
emp_2 = Employee('AN', 'Other', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# fname, lname, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
