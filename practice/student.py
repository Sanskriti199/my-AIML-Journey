class Student:
    college_name="abc" #class
    PI=3.1

    def __init__(self, name,gpa):
        self.name= name #instance
        self.gpa=gpa
        self.PI=3.14

stud1= Student("Rahul", 9.5)

print(Student.PI)#class
print(stud1.PI)#instance