class ShoppingCart:
    store_name = "Online Bazaar"
    tax_rate = 0.08
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
    def add_item(self, item_name, price):
        if price <= 0:
            print("Invalid price. Must be greater than 0")
        else:
            print(f"Added {item_name} (${price}) to cart")
            self.items.append({"name": item_name, "price": price})
    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item["name"] == item_name:
                self.items.pop(i)
                print(f"Removed {item_name} from cart")
                return
        print(f"Item '{item_name}' not found in cart")
    def get_subtotal(self):
        subt_price = 0
        for item in self.items:
            if item == self



