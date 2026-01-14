#The Report Generator
def generate_report(sales_data, filename):
    total = sum(sales_data.values())
    count = len(sales_data)
    average = total / count
    with open("sales_report.txt", "w") as f:
        f.write("WEEKLY SALES REPORT\n")
        f.write("-------------------\n")
        [f.write(f"{day}: ${amount:.2f}\n") for day, amount in sales_data.items()]
        f.write("-------------------\n")
        f.write(f"Total: ${total:.2f}\n")
        f.write(f"Average: ${average:.2f}")

     
sales = {"Mon": 100.50, "Tue": 200.00, "Wed": 150.75}
generate_report(sales, "sales_report.txt") 
