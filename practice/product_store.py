class Product:
    count=0
    def __init__(self, name, price):
        self.name= name
        self.price=price
        Product.count+=1

    def get_info(self):#instance method
        print(f"price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"total product is store ={cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price={price-(price*discount/100)}")

#this was the part1 of this question
p1=Product("Phone", 10_000)
p2=Product("Laptop", 40_000)
p3=Product("Pen", 10)

p1.calc_discount(p1.price,12)