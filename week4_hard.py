class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def apply_discount(self, discount_percentage):
        discount = self.price * discount_percentage / 100
        return self.price - discount

    def display_info(self):
        print(f"Ürün adı: {self.name}")
        print(f"Ürün fiyatı: {self.price}")
        print(f"Stok sayısı: {self.stock_quantity}")

class Customer:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_item(product, quantity)


    def place_order(self):
        self.shopping_cart.display_cart()
        print(f"Total price : {self.shopping_cart.calculate_total()}")
        print(f"Mail: {self.mail}")

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.name in self.items:
            if quantity > product.stock_quantity:
                print("Ürünün stok sayısı yetersiz!")
            else:
                quantity += 1
                self.items[product.name] = {"product" : product, "quantity" : quantity}

        else :
            if quantity > product.stock_quantity:
                print("Ürünün stok sayısı yetersiz!")
            else:
                self.items[product.name] = {"product" : product, "quantity" : quantity}

        product.stock_quantity -= quantity

    def display_cart(self):
        for product_name in self.items:
            print("Product: %s" % (product_name))
            print("Unit price: %f" % (self.items[product_name]["product"].price))
            print("Quantity: %d" % (self.items[product_name]["quantity"]))

    def calculate_total(self):
        total = 0
        for product_name in self.items :
            total += self.items[product_name]["quantity"] * self.items[product_name]["product"].price
        return total

laptop = Product("Laptop", 1200, 10)
phone = Product("Phone", 500, 20)

# Müşteri oluştur
customer1 = Customer("John Doe", "john@example.com")

# Ürünleri sepete ekle
customer1.add_to_cart(laptop, 2)
customer1.add_to_cart(phone, 3)

# Siparişi tamamla
customer1.place_order()





