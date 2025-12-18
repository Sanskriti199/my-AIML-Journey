class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
        self.gpa=gpa

class TA(Teacher, Student):
    def __init__(self, salary,gpa,name):
        super(). __init__(salary)
        Student.__init__(self,gpa)
        self.name=name

tal= TA(15_000, 9.3, "Sans")

print(tal.name, tal.gpa, tal.salary)

