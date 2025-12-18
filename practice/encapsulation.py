class BankAccount:
    def __init__(self, name, balance):
        self.name=name #public
        self._balance= balance #protected

    def get_balance(self): #getter to get value
        return self.__balance #private
    
    def set_balance(self, newBalance): #setter
        self.__balance = newBalance 

acc1= BankAccount("Rahul kumar", 1_00_000)

acc1.set_balance(200_000)
print(acc1.name,  acc1.get_balance())

#to access private variable
#print(acc1.name, acc1._BankAccount__balance)
