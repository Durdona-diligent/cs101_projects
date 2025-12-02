products = {
    "101": ("Milk", 2.50),
    "102": ("Eggs", 3.00),
    "103": ("Bread", 1.75),
    "104": ("Cheese", 4.50),
    "105": ("Apple", 0.50)
}

cart = ["101", "105", "105", "999", "103", "105"]
def receipt_gen(cart):
    total = 0
    for barcode_id in cart:
        if barcode_id in products:
            product_info = products[barcode_id]
            product_name = product_info[0]
            price = product_info[1]
            total += price
            print(f"{product_name}: ${price}")
        else:
            print(f"Item {barcode_id} not found")
    print("--------------------")
    print(f"Grand Total: ${total}")
print(receipt_gen(cart))
