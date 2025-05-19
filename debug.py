from customer import Customer
from coffee import Coffee
from order import Order



latte = Coffee("Latte")
cappucino = Coffee("Cappucino")

alex = Customer("Alex")
stacy = Customer("Stacy")
phillip = Customer("Phillip")



stacy.create_order(latte, 6.0)
alex.create_order(latte, 8.0)
alex.create_order(cappucino, 5.5)


order_one = Order(phillip, latte, 10.0)
order_two = Order(phillip, cappucino, 3.5)




print (latte.customers())
print(latte.average_price())
print(latte.num_orders())

print (phillip.coffees())

print(order_one.customer.name)
print(latte.orders()[2].customer.name)