from .order import Order


class Coffee:
    all_coffee = []
    
    def __init__(self, name):
        if (isinstance(name, str) and len(name) >= 3):
            self._name = name
            
    @property
    def name(self):
        return self._name
    
    def orders (self):
        return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self):
        return list({order.customer for o in self.orders()})
    
    def num_orders(self):
        return len(self.orders())