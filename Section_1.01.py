#University System – Student & Teacher
''' implementing the PCPP section 1
essential terminology: class, instance, object, attribute, method, type,
 instance and class variables, superclasses and subclasses
'''

class Person:
    university_name = "Symbiosis"
    def __init__(self,name,age):
        self.name = name
        self.age = age;

    def get_details(self):
        return print("Name is "+ self.name+"Age is "+ self.age)

    def speak(self):
        return print( self.name + " Says hello!")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_details(self):         # method overriding (polymorphism)
        return f"Student {self.name}, ID: {self.student_id}"

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def get_details(self):
        return print("Professor name is " + self.name);

student1 = Student("Alice",20,"S123")
teacher1 = Teacher("Dr. Bob", 45, "Physics")

print(student1.get_details())
print(teacher1.get_details())
print(student1.speak())
print(type(student1))            # Shows object type
print(isinstance(student1, Student))  # True
print(issubclass(Student, Person))   # True
print("University:", Student.university_name)
