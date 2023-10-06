# superclass
class Person():
    def __init__(self, per_name, per_age):
        self.name = per_name
        self.age = per_age
	
    def display1(self):
        print("name:", self.name)
        print("age:", self.age)

# subclass		
class Employee(Person):
    def __init__(self, emp_name, emp_age, emp_salary):
        self.salary = emp_salary
        super().__init__(emp_name, emp_age)
	
    def display2(self):
        print("salary:", self.salary)
        super().display1()
		
emp = Employee("John", 20, 8000)  # creating object of subclass

emp.display2()

emp.display1()