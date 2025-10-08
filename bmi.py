print("="*50)
print("          BMI CALCULATOR")
print("="*50)

name = input("Enter your name: ")
weight = float(input("weight (kg): "))
height = float(input("height (m): "))
bmi = weight/ (height ** 2)
is_underweight = bmi < 18.5
is_normal = bmi >= 18.5 and bmi < 25
is_overweight = bmi >= 25 and bmi < 30
is_obese = bmi >= 30

print(f"\n{'='*50}")
print(f"Results for {name}")
print(f"{'='*50}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")
print(f"{'='*50}")
print(f"Underweight (< 18.5): {is_underweight}")
print(f"Normal (18.5-24.9): {is_normal}")
print(f"Overweight (25-29.9): {is_overweight}")
print(f"Obese (>= 30): {is_obese}")
print(f"{'='*50}\n")