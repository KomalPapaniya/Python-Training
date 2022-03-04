class Person:
    def __init__(self, name, dob, city, contact_no):
        self.Name = name
        self.DOB = dob
        self.City = city
        self.Contact_No = contact_no

class Employee(Person):
    e_id = 101

    def __init__(self, name, dob, city, contact_no, joining_date, salary, dept, post):
        super().__init__(name, dob, city, contact_no)
        self.E_id = Employee.e_id
        self.Joining_Date = joining_date
        self.Salary = salary
        self.Department = dept
        self.Post = post

        Employee.e_id += 1

class EmployeeManager:
    def __init__(self):
        self.employee_list = []

    def get_all_employee(self):
        if len(se)

