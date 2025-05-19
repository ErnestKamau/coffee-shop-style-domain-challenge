class Coffee:
    all_coffee = []
    
    def __init__(self, name):
        if (isinstance(name, str) and len(name) >= 3):
            self._name = name
            Coffee.all_coffee.append(self)
            
    @property
    def name(self):
        return self._name
    
    def orders (self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self):
        return list({order.customer.name for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def  average_price(self):
        if len(self.orders()) >= 1:
            avg_price = (sum(order.price for order in self.orders())) / len(self.orders())
            return (f"Average price is {avg_price}")
        else:
            return None
    