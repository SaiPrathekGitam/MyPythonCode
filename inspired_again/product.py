# Program to illustrate classes


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_details(self):
        print(self.name, self.price)


# Creation of an object

p1 = Product('Paper Clip', 10)
p1.print_details()
# print(p1.name)
