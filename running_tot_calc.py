print("\n--- Running Total Calculator ---")
print()
print("Enter numbers to add them up. Type 'done' to see the total. ")
running_total=0
while True:
    response = input("Enter a number or 'done': ")
    if response =='done':
        break
    else:
         new_number = float(response)
    running_total+=new_number
    print(f"Current total: {running_total}")
print()
print("--- Final Calculation ---")
print(f"The final sum of all numbers is: {running_total}")