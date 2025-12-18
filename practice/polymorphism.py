#print(1+2, "hello"+"sans")
#that's how polymorphism works
#function overriding
class Employee: #parent class
    def get_designation(self):
        print("designation= Employee")

class Teacher(Employee): #student class
    def get_designation(self):
        print("designation= Teacher")

t1= Teacher()
t1.get_designation()