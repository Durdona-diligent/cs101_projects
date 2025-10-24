print("\n--- Triangle Pattern Printer ---")
height = int(input("Enter the desired height of the triangle: "))
for row_num in range(1, height + 1):
    for col_num in range(row_num):
         print("*", end=" ")
    print()