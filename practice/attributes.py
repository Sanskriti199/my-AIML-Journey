class Student:
    college_name="abc" #class

    def __init__(self, name,gpa):
        self.name= name #instance
        self.gpa=gpa

stud1= Student("Rahul", 9.5)

print(stud1.name, stud1.gpa)
print(stud1.college_name)