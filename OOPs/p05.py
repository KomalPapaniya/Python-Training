from datetime import date

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

    def remove(self, id):
        for emp in self.employee_list:
            if emp.E_id == id:
                print("Employee with Id {}, name {} removed".format(id, emp.Name))
                self.employee_list.remove(emp)
        
    def get_all_employee(self):
        if len(self.employee_list) == 0:
            print("Currently, no employee data exists...\n")
        else:
            for emp in self.employee_list:
                print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

    def find(self, value):
        for emp in self.employee_list:
            if value in emp.Name.split(" ") or value == str(emp.E_id) or value == emp.City or value == emp.Department or value == emp.Post or value == str(emp.Contact_No):
                print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))   

    def salary(self, value):
        if value.isnumeric():
            for emp in self.employee_list:
                if emp.Salary == int(value):
                    print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))   

        elif ">" in value:
            value = int(value.split(">")[1])
            for emp in self.employee_list:
                if emp.Salary > value:
                    print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

        elif "<" in value:
            value = int(value.split("<")[1])
            for emp in self.employee_list:
                if emp.Salary < value:
                    print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))   

        elif "-" in value:
            value = value.split("-")
            for emp in self.employee_list:
                if emp.Salary >= int(value[0]) and emp.Salary <= int(value[1]):
                    print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

        elif value == "asc":
            self.employee_list.sort(key=lambda x: x.Salary)
            for emp in self.employee_list:
                print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

        elif value == "desc":
            self.employee_list.sort(key=lambda x: x.Salary, reverse=True)
            for emp in self.employee_list:
                print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

    def joined_this_year(self):
        for emp in self.employee_list:
            if emp.Joining_Date.year == date.today().year:
                print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

    def dob_in_this_month(self):
        for emp in self.employee_list:
            if emp.DOB.month == date.today().month:
                print("Employee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))

manager_obj = EmployeeManager()

while True:
    task = int(input("0: Add Employee\n1: Show list of all Employees\n2: Search for Employee\n3: Remove Employee\n4: Quit\n"))
    if task == 4:
        break
    elif task == 0:
        name = input("Enter Name: ")
