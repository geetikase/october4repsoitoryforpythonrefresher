class Employee:
    def __init__(self, employee_name, employee_salary):
        self.employee_name = employee_name
        self.employee_salary = employee_salary

    def display_name(self):
        print(f"Employee Name: {self.employee_name}")

    def display_salary(self):
        print(f"Employee Salary: {self.employee_salary}")
