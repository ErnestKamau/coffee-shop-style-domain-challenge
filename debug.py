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
    
    
    def orders (self):
        return [order for order in Order.all_orders if order.customer == self]
    

    def create_order(self, coffee, price):
            return Order(self, coffee, price)
            
            
            
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
    

customer_one = Customer("Daniel")
customer_two = Customer("Alex")
coffee_one = Coffee("Cappuccino")
coffee_two = Coffee("Americano")
coffee_three = Coffee("Latte")

customer_two.create_order(coffee_three, 6.5)
print(customer_two.orders()[0].coffee.name)