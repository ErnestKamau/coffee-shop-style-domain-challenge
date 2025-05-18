from .order import Order


class Customer:
    all_customers = []
    
    def __init__(self, name):
        if (isinstance(name, str) and len(name) >=1 and len(name) <=15):
            self._name = name
            Customer.all_customers.append(self)
        else:
            print("Must be a string and between 1-15 charachters")
            
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
        
    def create_order(self, coffee, price):
            return Order(self, coffee, price)
    
    def orders (self):
        return [order for order in Order.all_orders if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})