class student:
    count = 0;
    def __init__(self,name):
        self.name = name;
        student.count += 1;

    @classmethod
    def get_student_count(cls):
        return cls.count;

s1 = student("D1")
s2 = student("D2")

print(student.get_student_count())