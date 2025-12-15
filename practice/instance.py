class Laptop:
    storage_type="ssd"

    def __init__(self, RAM, storage):
        self. RAM= RAM
        self. storage= storage

    def get_info(self): #instance method has accessed instance as well as class attributes
        print(f"laptop has {self.RAM} RAM &{self.storage}, {self.storage_type}")

l1= Laptop("16gb", "512gb")
l2= Laptop("8gb", "256gb")

l1.get_info()
