class Product:
    # Constructor
    def __init__(self, name, price=0):
        # Object Attributes
        self.name = name
        self.price = price

    def print_details(self):
        print(f"Name  : {self.name}")
        print(f"Price : {self.price}")

    def net_price(self):
        return round(self.price * 1.12)


p1 = Product("Product One", 10000)
p1.print_details()
print(p1.net_price())
print(p1.name)