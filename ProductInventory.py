# Product Inventory Project - Create an application which manages an inventory of products. Create a product class which has a price,
# id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product:

    def __init__(self, price, id, quantity):

        self.price = price
        self.id = id
        self.quantity = quantity


class Inventory(Product):

    def __init__(self):
        super().__init__()

    def sum_value(self):
        return self.price * self.quantity


motor = Product(1000, 23, 5)
car = Product(30000, 2, 6)
overall = Inventory