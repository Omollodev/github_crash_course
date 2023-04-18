
class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def full_name(self):
        print(f"My full name is {self.fname}{self.lname}")

    def email(self):
        print(f"{self.fname}{self.lname} @gmail.com")


emp_1 = Employee('correy', 'scharfer', 50000)
emp_1.full_name()
emp_1.email()
