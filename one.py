class one:

    pay_rate = 0.8
    
    def __init__(self,name:str,price:int,quantity):
        
        assert price > 0, f"Price {price} less than 1"
        assert quantity > 0, f"Quantity{quantity} less than 1"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return(self.price*self.quantity)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
ins = one(1,5)

print(ins.__dict__)


