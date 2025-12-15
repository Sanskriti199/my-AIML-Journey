class Laptop:
    storage_type="ssd"

    def __init__(self, RAM, storage):
        self. RAM= RAM
        self. storage= storage

    @classmethod #changed the below function in the class method
    def get_storage_type(cls):
        print(f"storage type={cls.storage_type}")

    def get_info(self): #instance method has accessed instance as well as class attributes
        print(f"laptop has {self.RAM} RAM &{self.storage}, {self.storage_type}")

l1= Laptop("16gb", "512gb")


Laptop.get_storage_type()
l1.get_storage_type()
