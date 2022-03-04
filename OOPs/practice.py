
import datetime 
from datetime import date
class Person():
    def __init__(self,name,dob,city,contact_no):
        self.name = name
        self.dob = dob
        self.city = city
        self.contact_no = contact_no
        
class Employee(Person):
    employee_id = 1111
    def __init__(self, name, dob, city, contact_no,joining_date,salary,department,post):
        super().__init__(name, dob, city, contact_no)
        self.employee_id = Employee.employee_id
        self.joining_date = joining_date
        self.salary = salary
        self.department = department
        self.post = post
        Employee.employee_id += 1
        
class EmployeeManager():
    def __init__(self):
        self.employee_list = []
        
    def show_all_employee(self):
        if len(self.employee_list) != 0:
            for employee_obj in self.employee_list:
                print(f'Employee id: [{employee_obj.employee_id}]',
                    f'Name: [{employee_obj.name}]',
                    f'Date of birth: [{employee_obj.dob}]',
                    f'City: [{employee_obj.city}]',
                    f'Contact No.: [{employee_obj.contact_no}]',
                    f'Joining date: [{employee_obj.joining_date}]',
                    f'Salary: [{employee_obj.salary}]',
                    f'Department: [{employee_obj.department}]',
                    f'Post: [{employee_obj.post}]\n',
                    )
        else:
            print('No such data exist!\n')
            
    def search(self,value):
        for employee_obj in self.employee_list:
            if (value in employee_obj.name) or (value == str(employee_obj.employee_id)) or (value == employee_obj.city) or (value == employee_obj.department) or (value == employee_obj.post) or (value == str(employee_obj.contact_no)):
                print(f'Employee id: [{employee_obj.employee_id}]',
                    f'Name: [{employee_obj.name}]',
                    f'Date of birth: [{employee_obj.dob}]',
                    f'City: [{employee_obj.city}]',
                    f'Contact No.: [{employee_obj.contact_no}]',
                    f'Joining date: [{employee_obj.joining_date}]',
                    f'Salary: [{employee_obj.salary}]',
                    f'Department: [{employee_obj.department}]',
                    f'Post: [{employee_obj.post}]\n',
                    )
                
    def find_salary(self,value):
        if '>' in value:
            value = value.split('>')
            for employee_obj in self.employee_list:
                if int(employee_obj.salary) > int(value[1]):
                    print(f'Employee id: [{employee_obj.employee_id}]',
                        f'Name: [{employee_obj.name}]',
                        f'Date of birth: [{employee_obj.dob}]',
                        f'City: [{employee_obj.city}]',
                        f'Contact No.: [{employee_obj.contact_no}]',
                        f'Joining date: [{employee_obj.joining_date}]',
                        f'Salary: [{employee_obj.salary}]',
                        f'Department: [{employee_obj.department}]',
                        f'Post: [{employee_obj.post}]\n',
                        )
        elif '<' in value:
            value = value.split('<')
            for employee_obj in self.employee_list:
                if int(employee_obj.salary) < int(value[1]):
                    print(f'Employee id: [{employee_obj.employee_id}]',
                        f'Name: [{employee_obj.name}]',
                        f'Date of birth: [{employee_obj.dob}]',
                        f'City: [{employee_obj.city}]',
                        f'Contact No.: [{employee_obj.contact_no}]',
                        f'Joining date: [{employee_obj.joining_date}]',
                        f'Salary: [{employee_obj.salary}]',
                        f'Department: [{employee_obj.department}]',
                        f'Post: [{employee_obj.post}]\n',
                        )
        elif '-' in value:
            value = value.split('-')
            for employee_obj in self.employee_list:
                if int(employee_obj.salary) > int(value[0]) and int(employee_obj.salary) < int(value[1]):
                    print(f'Employee id: [{employee_obj.employee_id}]',
                        f'Name: [{employee_obj.name}]',
                        f'Date of birth: [{employee_obj.dob}]',
                        f'City: [{employee_obj.city}]',
                        f'Contact No.: [{employee_obj.contact_no}]',
                        f'Joining date: [{employee_obj.joining_date}]',
                        f'Salary: [{employee_obj.salary}]',
                        f'Department: [{employee_obj.department}]',
                        f'Post: [{employee_obj.post}]\n',
                        )
        elif 'i' == value:
            for index_i,employee_obj_i in enumerate(self.employee_list):
                for index_j,employee_obj_j in enumerate(self.employee_list):
                    if employee_obj_i.salary < employee_obj_j.salary:
                        self.employee_list[index_i],self.employee_list[index_j] = self.employee_list[index_j],self.employee_list[index_i]
                        
            self.show_all_employee()
            
        elif 'd' == value:
            for index_i,employee_obj_i in enumerate(self.employee_list):
                for index_j,employee_obj_j in enumerate(self.employee_list):
                    if employee_obj_i.salary > employee_obj_j.salary:
                        self.employee_list[index_i],self.employee_list[index_j] = self.employee_list[index_j],self.employee_list[index_i]
                        
            self.show_all_employee()

    def find_year(self):
        for employee_obj in self.employee_list:
            if employee_obj.joining_date.year == date.today().year:                
                print(f'Employee id: [{employee_obj.employee_id}]',
                    f'Name: [{employee_obj.name}]',
                    f'Date of birth: [{employee_obj.dob}]',
                    f'City: [{employee_obj.city}]',
                    f'Contact No.: [{employee_obj.contact_no}]',
                    f'Joining date: [{employee_obj.joining_date}]',
                    f'Salary: [{employee_obj.salary}]',
                    f'Department: [{employee_obj.department}]',
                    f'Post: [{employee_obj.post}]\n',
                    )
    def find_dob_current(self):
        for employee_obj in self.employee_list:
            if employee_obj.dob.month == date.today().month: 
                print(f'Employee id: [{employee_obj.employee_id}]',
                    f'Name: [{employee_obj.name}]',
                    f'Date of birth: [{employee_obj.dob}]',
                    f'City: [{employee_obj.city}]',
                    f'Contact No.: [{employee_obj.contact_no}]',
                    f'Joining date: [{employee_obj.joining_date}]',
                    f'Salary: [{employee_obj.salary}]',
                    f'Department: [{employee_obj.department}]',
                    f'Post: [{employee_obj.post}]\n',
                    )
    def remove_employee(self,id):
        for employee_obj in self.employee_list:
            if int(employee_obj.employee_id) == id: 
                print(f'Employee id: [{employee_obj.employee_id}]',
                    f'Name: [{employee_obj.name}]','Deleted succesfully!!!\n'
                    )
                self.employee_list.remove(employee_obj)
                   
object_of_manager = EmployeeManager()

while True:
    try:
        operation = int(input('Enter 0: Add new Employee\nEnter 1: See all Employees\nEnter 2: Search\nEnter 3: Remove user\nEnter 4: Quit\n:)'))
        print('')
        if operation>4 or operation<0:   
            raise Exception
        elif not operation:         
            name = input('Enter name: ')
            while True:
                try:
                    dob = input('Enter Date of birth (in DD/MM/YYYY): ')
                    dob=datetime.datetime.strptime(dob,"%d/%m/%Y").date()
                    break
                except Exception:
                    print('Please, Enter date in right format (DD/MM/YYYY) - (02/02/2000)')
            city = input('Enter city: ')
            contact_no = int(input('Enter Contact No.: '))
            while True:
                try:
                    joining_date = input('Enter Joining date (in DD/MM/YYYY): ')
                    joining_date=datetime.datetime.strptime(joining_date,"%d/%m/%Y").date()
                    break
                except Exception:
                    print('Please, Enter date in right format (DD/MM/YYYY) - (02/02/2000)')
            salary = int(input('Enter salary: '))
            department = input('Enter Department: ')
            post = input('Enter post: ')
            object_of_employee = Employee(name,dob,city,contact_no,joining_date,salary,department,post)
            object_of_manager.employee_list.append(object_of_employee)
            print('\n')
        elif operation == 1:
            object_of_manager.show_all_employee()
        elif operation == 2:
            while True:
                try:
                    operation_search = int(input('Enter 0: Search by Name|City|Employee Id|Contact No|Department|Post\nEnter 1: Search by salary\nEnter 2: Search by Joining Year\nEnter 3: See Employee\'s birthday in current month\nEnter 4: back\n:)'))
                    if operation_search > 4 or operation_search < 0:
                        print('Please Enter only 0,1,2,3 or 4\n')
                    elif not operation_search:
                        search = input('Search by Name|City|Employee Id|Contact No|Department|Post\n:)')
                        object_of_manager.search(search)
                    elif operation_search == 1:
                        search_salary = (input('- If you want to find great/less then salary than write \'>value or <value\'\n- If you want find salary between some value then write \'value-value\'\n- If want find salara increasing/decreasing order then write i/d\n:)'))
                        object_of_manager.find_salary(search_salary)
                    elif operation_search == 2:
                        object_of_manager.find_year()
                    elif operation_search == 3:
                        object_of_manager.find_dob_current()
                    elif operation_search == 4:
                        break    
                except Exception:
                    print('Please Enter only 0,1 or 2\n', type(e).__name__,e)
        elif operation == 3:
            employee_id = int(input('Enter employee id: '))
            confirmation = (input(f'Are you sure you want delete record of {employee_id} : y/n'))
            if confirmation == 'y':
                object_of_manager.remove_employee(employee_id)             
        elif operation == 4:
            break
    except Exception as e:
        print('Please Enter only 0,1 or 2\n', type(e).__name__,e)