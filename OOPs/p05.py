import datetime
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
                print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
    def find(self, value):
        for emp in self.employee_list:
            if value in emp.Name or value == str(emp.E_id) or value == emp.City or value == emp.Department or value == emp.Post or value == str(emp.Contact_No):
                print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))  
 
    def salary(self, value):
        if value.isnumeric():
            for emp in self.employee_list:
                if emp.Salary == int(value):
                    print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))  
 
        elif ">" in value:
            value = int(value.split(">")[1])
            for emp in self.employee_list:
                if emp.Salary > value:
                    print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
        elif "<" in value:
            value = int(value.split("<")[1])
            for emp in self.employee_list:
                if emp.Salary < value:
                    print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))  
 
        elif "-" in value:
            value = value.split("-")
            for emp in self.employee_list:
                if emp.Salary > int(value[0]) and emp.Salary < int(value[1]):
                    print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
        elif value == "asc":
            self.employee_list.sort(key=lambda x: x.Salary)
            for emp in self.employee_list:
                print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
        elif value == "desc":
            self.employee_list.sort(key=lambda x: x.Salary, reverse=True)
            for emp in self.employee_list:
                print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
    def joined_this_year(self):
        for emp in self.employee_list:
            if emp.Joining_Date.year == date.today().year:
                print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
    def dob_in_this_month(self):
        for emp in self.employee_list:
            if emp.DOB.month == date.today().month:
                print("\nEmployee Id: {} | ".format(emp.E_id), "Name: {} | ".format(emp.Name), "DOB: {} | ".format(emp.DOB), "City: {} | ".format(emp.City), "Contact Details: {} | ".format(emp.Contact_No), "Joining Date: {} | ".format(emp.Joining_Date), "Salary: {} | ".format(emp.Salary), "Department: {} | ".format(emp.Department), "Post: {}".format(emp.Post))
 
manager_obj = EmployeeManager()
 
while True:
    try:
        task = int(input("\n0: Add Employee\n1: Show list of all Employees\n2: Search for Employee\n3: Remove Employee\n4: Quit\n"))
        if task == 4:
            break
   
        elif task == 0:
            name = input("Enter Name: ")
            while True:
                try:
                    dob = input('Enter Date of birth in DD/MM/YYYY Format: ')
                    dob = datetime.datetime.strptime(dob,"%d/%m/%Y").date()
                    break
                except Exception:
                    print('Please, Enter date in DD/MM/YYYY format. Example: (06/11/2000)')
 
            city = input("Enter City: ")
            contact = int(input('Enter Contact Details.: '))
            while True:
                try:
                    j_date = input('Enter Joining Date in DD/MM/YYYY Format: ')
                    j_date = datetime.datetime.strptime(j_date,"%d/%m/%Y").date()
                    break
                except Exception:
                    print('Please, Enter date in DD/MM/YYYY format. Example: (06/11/2000)')
 
            salary = int(input('Enter Salary: '))
            dept = input('Enter Department: ')
            post = input('Enter Post: ')
            emp_obj = Employee(name, dob, city, contact, j_date, salary, dept, post)
            manager_obj.employee_list.append(emp_obj)
   
        elif task == 1:
            manager_obj.get_all_employee()
   
        elif task == 2:
            while True:
                try:
                    operation = int(input("\n0: Search by Employee Details\n1: Search by Salary\n2: Search by Joining Year\n3: Search for Employees having birthday in current month\n4: back\n"))
                    if operation == 4:
                        break
                    elif operation == 0:
                        search = input("\nSearch by Name, City, Employee Id, Contact No, Department, Post\n")
                        manager_obj.find(search)
                    elif operation == 1:
                        salary_operation = input("\n-> Enter salary to search by salary\n-> Enter 'salary-salary' to search by salary range\n-> Enter '>' to search for salary greater than given ammount\n-> Enter '<' to search for salary less than given ammount\n-> Enter 'asc' to view employee details in ascending order of salary\n-> Enter 'desc' to view employee details in descending order of salary\n")
                        manager_obj.salary(salary_operation)
                    elif operation == 2:
                        manager_obj.joined_this_year()
                    elif operation == 3:
                        manager_obj.dob_in_this_month()
                except Exception:
                    print("Please select correct option\n", type(Exception).__name__,Exception)
   
        elif task == 3:
            id = int(input('Enter id of the Employee you want to remove: '))
            manager_obj.remove(id)
 
        else:
            raise Exception
           
    except Exception:
        print("Please select correct option\n", type(Exception).__name__,Exception)
           
 

