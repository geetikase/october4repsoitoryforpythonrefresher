class Student:
    def __init__(self, name, age, studentid):
        self.name = name
        self.age = age
        self.studentid = studentid
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.studentid}")
