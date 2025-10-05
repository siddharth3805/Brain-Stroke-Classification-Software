class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added.")

    def update_stock(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.quantity += quantity
                print(f"Stock updated. New quantity of {product.name}: {product.quantity}")
                return
        print("Product not found.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product {product.name} removed.")
                return
        print("Product not found.")

    def check_stock_levels(self):
        for product in self.products:
            print(f"{product.name}: {product.quantity}")

    def calculate_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"Total inventory value: {total}")

# Example usage:
inv = Inventory()
prod1 = Product("Pen", 10, 100)
prod2 = Product("Notebook", 50, 200)
inv.add_product(prod1)
inv.add_product(prod2)
inv.update_stock("Pen", 50)
inv.check_stock_levels()
inv.calculate_inventory_value()
inv.remove_product("Pen")
inv.check_stock_levels()
