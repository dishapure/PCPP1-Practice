# Single Inheritance

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}, ID: {self.id}")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)  # Using super() to call base class constructor
        self.department = department

    def display_role(self):
        print(f"{self.name} is a manager of the {self.department} department.")

# Multiple Inheritance

class Developer:
    def __init__(self, language):
        self.language = language

    def code(self):
        print(f"Coding in {self.language}")

class Designer:
    def __init__(self, tool):
        self.tool = tool

    def design(self):
        print(f"Designing with {self.tool}")

class TechLead(Developer, Designer):
    def __init__(self, name, language, tool):
        Developer.__init__(self, language)
        Designer.__init__(self, tool)
        self.name = name

    def lead_team(self):
        print(f"{self.name} is leading the tech team.")

# Main Program

print("=== Single Inheritance ===")
mgr = Manager("Alice", 1001, "Sales")
mgr.display_info()
mgr.display_role()

print("\n=== Multiple Inheritance ===")
lead = TechLead("Bob", "Python", "Figma")
lead.code()
lead.design()
lead.lead_team()

# Comment on the difference between single and multiple inheritance
print("\n=== Difference Between Inheritance Types ===")
print("Single Inheritance allows a class to inherit from one parent class.")
print("Multiple Inheritance allows a class to inherit from more than one parent class.")
print("Python supports both, but multiple inheritance can be tricky if both parents have methods with the same name.")
