class Student:
    def __init__(self): #default constructor
        print("Object is constructed...")

    def __init__(self, name, cgpa):# parameterized constructor
        self.name= name
        self.cgpa=cgpa

    def get_cgpa(self): #instance methodss
        return self.cgpa

stud1= Student("Rahul", 9.0)
stud2= Student("jeet", 9.3)
stud3= Student("Aarohi", 9.5)

print(f"{stud1.name} has cgpa = {stud1.get_cgpa()}")
