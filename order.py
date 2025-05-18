from .customer import Customer
from .coffee import Coffee


class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        
        if (isinstance(price, float) and price >=1.0 and price <= 10.0):
            self.customer = customer
            self.coffee = coffee
            self._price = price
            Order.all_orders.append(self)
        else:
            raise TypeError("Price must be a float and between 1.0 and 10.0")
        
    
    @property
    def price(self):
        return self._price