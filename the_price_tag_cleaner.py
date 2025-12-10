def sum_valid_prices(price_list):
    total = 0
    for item in price_list:
        if item == "Free":
            continue
        if "$" in item:
            cleaned_item = item.replace("$", "")
        else:
            cleaned_item = item
        try:
            float_item = float(cleaned_item)
        except ValueError:
            print((f"Skipping invalid price: [{cleaned_item}]"))
            continue
        total += float_item
    return total

raw_prices = ["$12.50", "Free", "error_404", "$5.00", "2.50", "N/A"]
total = sum_valid_prices(raw_prices)
print(f"Total: ${total}")